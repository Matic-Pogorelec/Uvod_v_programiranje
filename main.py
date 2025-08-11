import re
import requests
import gender_guesser.detector as gender
d = gender.Detector()
print("Delam, ne me motit")
def zlepi(seznam):
    if seznam == []:
        return ""
    else:
        return seznam[0] + zlepi(seznam[1:])
def odstrani_vejice_in_intigiraj(niz):
    return(int(zlepi(niz.split(","))))
tabela_skupna = []
tabela_razdelki = []
for i in range(1,2):
    tabela = []
    šahisti = requests.get(f"https://www.chess.com/callback/leaderboard/live/rapid?gameType=live&page={i}&totalPage=10000")
    šahisti_2 = šahisti.text
    vzorec = r'\{"user":.*?(?=,\{"user"|$)'
    tabela = re.findall(vzorec,šahisti_2)
    tabela_skupna = tabela_skupna + tabela
i = 0
for šahist in tabela_skupna:
    vzorec_rang = r'"rank":(\d*)'
    šahist_rang = re.search(vzorec_rang,šahist).group(1)
    if int(šahist_rang)%100 == 0:
        print(f"{int(šahist_rang)//100}/25")
    šahist_username_vzorec = r'"username":([^,]*)'
    šahist_username = re.search(šahist_username_vzorec, šahist).group(1)
    elo_vzorec = r'"score":(\d*)'
    elo = re.search(elo_vzorec,šahist).group(1)
    id_vzorec = r'"id":(\d*)'
    id = re.search(id_vzorec,šahist).group(1)
    država_vzorec = r'"country_name":([^,]*)'
    država_številka_vzorec = r'"country_id":(\d*)'
    država_številka = int(re.search(država_številka_vzorec,šahist).group(1))
    država =re.search(država_vzorec,šahist).group(1)
    naslov_vzorec = r'"chess_title":([^,]*)'
    naslov = "brez_naziva"
    if re.search(naslov_vzorec,šahist) != None:
        naslov = (re.search(naslov_vzorec,šahist).group(1))[1:-1]
    skupaj_igre_vzorec = r'"totalGameCount":(\d*)'
    skupaj_igre = re.search(skupaj_igre_vzorec,šahist).group(1)
    skupaj_zmage_vzorec = r'"totalWinCount":(\d*)'
    skupaj_porazi_vzorec = r'"totalLossCount":(\d*)'
    skupaj_remi_vzorec = r'"totalDrawCount":(\d*)'
    skupaj_zmage = int((re.search(skupaj_zmage_vzorec,šahist).group(1)))
    skupaj_porazi = int((re.search(skupaj_porazi_vzorec,šahist).group(1)))
    skupaj_remiji = int((re.search(skupaj_remi_vzorec,šahist).group(1)))
    strela_elo_vzorec = r'"key":"lightning","stats":\{"rating":(\d*)'
    metek_elo_vzorec = r'"key":"bullet","stats":\{"rating":(\d*)'
    besedilo = requests.get(f"https://www.chess.com/callback/member/stats/{šahist_username[1:-1]}").text
    strela_elo = "Ne igra strele"
    metek_elo = "Ne igra metka"
    skoraj_strela = re.search(strela_elo_vzorec,besedilo) 
    skoraj_metek = re.search(metek_elo_vzorec,besedilo)
    if skoraj_strela != None:
        strela_elo = int(skoraj_strela.group(1))
    if skoraj_metek != None:
        metek_elo = int(skoraj_metek.group(1))
    za_ime = (requests.get(f"https://www.chess.com/member/{šahist_username[1:-1]}/stats/rapid?days=90"))
    datoteka_za_ime = za_ime.text
    ime_vzorec = r'firstName: "([^,]*)"'
    priimek_vzorec = r'lastName: "([^,]*)"'
    ime = "Ni javen podatek"
    priimek = "Ni javen podatek"
    ime_skoraj = re.search(ime_vzorec, datoteka_za_ime)
    priimek_skoraj = re.search(priimek_vzorec, datoteka_za_ime)
    if priimek_skoraj != None:
        priimek = priimek_skoraj.group(1)
    if ime_skoraj != None:
        ime = ime_skoraj.group(1)
    opazovalci = "ni_javno"
    opazovalci_vzorec =  r'<div class="profile-header-details-value">(.*)</div> Views'
    skoraj_opazovalci = re.search(opazovalci_vzorec, datoteka_za_ime)
    if skoraj_opazovalci != None:
        opazovalci = skoraj_opazovalci.group(1)
    tabela_razdelki.append([int(šahist_rang),šahist_username[1:-1],ime, priimek, int(elo),id,država[1:-1],država_številka,naslov,int(skupaj_igre),skupaj_zmage,skupaj_porazi,skupaj_remiji,strela_elo,metek_elo,odstrani_vejice_in_intigiraj(opazovalci)])
    
for številka in range(len(tabela_razdelki)):
   if " " in tabela_razdelki[številka][2] and tabela_razdelki[številka][3] == "":
        ime_in_priimek = tabela_razdelki[številka][2].split()
        print(ime_in_priimek)
        tabela_razdelki[številka][2], tabela_razdelki[številka][3] = ime_in_priimek[0], ime_in_priimek[1]
print(tabela_razdelki)
moški_skupno = 0
ženskse_skupno = 0
ostalo = 0
for oseba in tabela_razdelki:
    ime = ""
    if oseba[2] != "":
        ime = ((oseba[2]).split())[0]
    if d.get_gender(ime) in {"male", "mostly_male"}:
        moški_skupno = moški_skupno + 1
    elif d.get_gender(ime) in {"female", "mostly_female"}:
        ženskse_skupno = ženskse_skupno + 1
        print(f"{oseba[2]} {oseba[3]}-{d.get_gender(ime)}")
    else:
        ostalo = ostalo + 1
    
print(moški_skupno)
print(ženskse_skupno)
print(ostalo)
print(requests.get(f"https://www.chess.com/callback/leaderboard/live/rapid?gameType=live&page={1}&totalPage=10000").text)
#naredi queary za https://www.chess.com/callback/member/stats/{username}
#ideja lahko narišeš graf, highest winning opponent
#v totem filu ko ga ze mas za ime najdes se sledilce in oglede
