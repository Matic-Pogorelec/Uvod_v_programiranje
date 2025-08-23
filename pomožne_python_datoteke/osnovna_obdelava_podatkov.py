import re
import requests
import pomožne_python_datoteke.spol_funkcije as spol_funkcije
import pomožne_python_datoteke.države_funkcije as države_funkcije
import pomožne_python_datoteke.čas_funkcije as čas_funkcije

def poberi_podatke():
    """ Funkicja s spleta pobere podatke in jih shrani v tabelo.

    funkcija gre na chess.com in iz html-ja pobere informacije o šahistih. O vsakem shrani rang, uporabniško ime, elo (za pospešeno),
    id šahista, ime države, neko številko, ki je asociirana z državo, število odigranih iger, število zmag/remijev/porazov, naslov šahista.
    podatke shrani v seznamu in ta seznam vrne"""
    tabela_skupna = []
    tabela_razdelki = []
    for i in range(1,31):
        tabela = []
        šahisti = requests.get(f"https://www.chess.com/callback/leaderboard/live/rapid?gameType=live&page={i}&totalPage=10000").text
        vzorec_šahist = r'\{"user":.*?(?=,\{"user"|$)'
        tabela = re.findall(vzorec_šahist,šahisti)
        tabela_skupna = tabela_skupna + tabela
    for šahist in tabela_skupna:
        tabela_za_šahista = []
        rang_vzorec = r'"rank":(\d*)'
        šahist_username_vzorec = r'"username":"([^,]*)"'
        elo_vzorec = r'"score":(\d*)'
        id_vzorec = r'"id":(\d*)'
        država_vzorec = r'"country_name":"([^,]*)"'
        država_številka_vzorec = r'"country_id":(\d*)'
        skupaj_zmage_vzorec = r'"totalWinCount":(\d*)'
        skupaj_porazi_vzorec = r'"totalLossCount":(\d*)'
        skupaj_remi_vzorec = r'"totalDrawCount":(\d*)'
        skupaj_igre_vzorec = r'"totalGameCount":(\d*)'
        seznam_1 = [rang_vzorec,šahist_username_vzorec, elo_vzorec, id_vzorec, država_vzorec,
                     država_številka_vzorec,skupaj_igre_vzorec,skupaj_zmage_vzorec,skupaj_remi_vzorec,skupaj_porazi_vzorec]
        for vzorec in seznam_1:
            tabela_za_šahista.append(re.search(vzorec,šahist).group(1))
        naslov_vzorec = r'"chess_title":"([^,]*)"'
        naslov = "Nima naslova"
        vzorec = re.search(naslov_vzorec,šahist)
        if vzorec != None:
            naslov = (vzorec.group(1))
        tabela_za_šahista.append(naslov)
        tabela_razdelki.append(tabela_za_šahista)
    return tabela_razdelki


def dodatni_podatki():
    """Funkcija pobere dodatne podatke.

    Požene poberi_podatke() in se sprehodi čez vse šahiste. Za vsakega šahsita gre na njegovo stran na chess.com
    (oziroma na dve) in iz nje pobere še dodatne podatke, med drugim ime, priimek, število ogledov, elo v drugih disciplinah...
    Podatke shrani skupaj z podatki iz poberi_podatke() v seznam."""
    tabela_razširjena = []
    tabela_razdelki = poberi_podatke()
    for šahist in tabela_razdelki:
        tabela_za_šahista = []
        besedilo_1 = requests.get(f"https://www.chess.com/callback/member/stats/{šahist[1]}").text
        besedilo_2 =(requests.get(f"https://www.chess.com/member/{šahist[1]}")).text
        besedili = (besedilo_1,besedilo_2)
        strela_elo_vzorec = r'"key":"lightning","stats":\{"rating":(\d*)'
        metek_elo_vzorec = r'"key":"bullet","stats":\{"rating":(\d*)'
        ime_vzorec = r'firstName: "([^"]*)"'
        priimek_vzorec = r'lastName: "([^,]*)"'
        opazovalci_vzorec =  r'<div class="profile-header-details-value">(.*)</div> Views'
        datum_vzorec = r'<div class="profile-header-details-value">(.*)</div> Joined'
        seznam_1 = [strela_elo_vzorec, metek_elo_vzorec]
        seznam_2 = [ime_vzorec, priimek_vzorec, opazovalci_vzorec, datum_vzorec]
        seznam_praznih_vrednosti = {strela_elo_vzorec: "Ne igra strele", metek_elo_vzorec: "Ne igra metka", ime_vzorec: "Ni javno", priimek_vzorec:"Ni javno", opazovalci_vzorec: "Ni javno", datum_vzorec: "Ni javno"}
        for vzorec in seznam_1 + seznam_2:
            število = 0 if vzorec in seznam_1 else 1
            iskanje = seznam_praznih_vrednosti[vzorec]
            regex = re.search(vzorec,besedili[število]) 
            if regex != None:
                iskanje = regex.group(1)
            tabela_za_šahista.append(iskanje)
        tabela_razširjena.append(šahist + tabela_za_šahista) 
    return tabela_razširjena


def končni_podatki_in_olepšava():
    """Doda nove in poleša obstoječe podatke"""
    celine = države_funkcije.celine()
    iz_števil_v_kode = države_funkcije.tabela_iz_števil_v_kode()
    koda_v_ime = države_funkcije.wikipedia_države_in_kode()
    populacija = države_funkcije.wikipedia_populacija()
    obrat_populacije = lambda x: države_funkcije.obratna_vrednost_prebivalstva(x,tabela_1=iz_števil_v_kode, tabela_2=koda_v_ime,tabela_3=populacija)
    tabela = dodatni_podatki()
    for i in range(len(tabela)):  
        if " " in tabela[i][13] and tabela[i][14] == "":
            ime_in_priimek = (tabela[i][13]).split() 
            tabela[i][13], tabela[i][14] = ime_in_priimek[0], ime_in_priimek[1]
        # Dodamo spol za šahiste.
        tabela[i].append(spol_funkcije.določi_spol(tabela[i][13]))
        # Dodamo celino.
        tabela[i].append(celine.get(iz_števil_v_kode[tabela[i][5]],"Ni podatka"))
        # Dodajmo obratno vrednost prebivalstva države.
        tabela[i].append(obrat_populacije(tabela[i][5]))
        # Spremenimo tip datuma.
        tabela[i][16] = čas_funkcije.spremeni_tip_datuma(tabela[i][16])
        # Sedaj lahko dodamo še leto.
        tabela[i].append(tabela[i][16][0:4])
        # Olepšamo še imena, priimke, uporabniška imena, države in oglede.
        slovar = {"O&#039;": "'","&quot;":'"',",":'',"\n":"","\\u00fc":"ü"}
        for zamenjano, zamenjava in slovar.items():
            for število in {4,13,14,2,15}:
                tabela[i][število] = tabela[i][število].replace(zamenjano,zamenjava)
    return tabela


def zapiši_podatke():
    """Požene končni_podatki_in_olepšava() in podatke prepiše v datoteko "Glavna_tabela.csv".""" 
    tabela = končni_podatki_in_olepšava()
    with open("csv_datoteke/Glavna_tabela.csv","w",encoding="UTF-8") as dat:
        besedilo = "Rang,Uporabniško ime,Elo,Id,Država,Država številka,Skupaj igre,Skupaj zmage,\
Skupaj remiji,Skupaj porazi,Naslov,Strela elo,Metek elo,Ime,Priimek,Opazovalci,\
Datum,Spol,Celina,Obratna vrednost prebivalstva,Leto\n"
        dat.write(besedilo)
        for šahist in tabela:
            besedilo_šahist = ""
            for podatek in šahist:
                besedilo_šahist = besedilo_šahist +","+ str(podatek)
            besedilo_šahist = besedilo_šahist[1:] + "\n"
            dat.write(besedilo_šahist)
