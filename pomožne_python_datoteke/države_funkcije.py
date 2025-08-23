import re
import requests

def tabela_iz_števil_v_kode():
    """Pobere podatke o številkah ki predstavljajo države  in alpha-2 kodah, s spleta in jih spravi v slovar.

    Funkcija iz https://www.chess.com/leaderboard/live/rapid in najde v njej del besedila, ki prikazuje katera
    Ključi so števila, vrne pa alpha-2 kodo države 
    funckija vrne slovar"""
    tabela = {}
    vzorec = r'"id":(\d*),"code":"([A-Z][A-Z])"'
    besedilo = (requests.get(("https://www.chess.com/leaderboard/live/rapid")).text)
    for besedilo in re.finditer(vzorec,besedilo):
        tabela[(besedilo.group(1))] = besedilo.group(2)
    return tabela


def wikipedia_države_in_kode():
    """Pobere podatke o alpha-2 kodah in imenih držav.

    Funkcija pobere HTML iz "https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes" in izbrska iz tabele ime
    in alpha-2 kodo za vsako državo. Podatke shrani v obliki slovarja. Ključi so alpha-2 kode, slovar pa vrne ime države
    Funkcija vrne slovar"""
    države_file = requests.get("https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes").text
    vzorec = r' title="(.*?)">.*?</a>.*?\n</td>\n<td>.*?\n</td>\n<td><a href="/wiki/ISO_3166-1_alpha-2\#([A-Z][A-Z])"'
    slovar_kod_in_imen = {}
    for j in re.finditer(vzorec,države_file):
          ime_države = j.group(1)
          if "(" in ime_države:
               ime_države = ime_države[:ime_države.index("(")-1]
          slovar_kod_in_imen[j.group(2)] = (ime_države)
    return(slovar_kod_in_imen)


def wikipedia_populacija():
    """Pobere podatke o imenih držav in številu prebivalcev.

    Funkcija pobere HTML iz "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population" in izbrska
    ime in število prebivalcev za vsako državo. Podatke shrani v obliki slovarja, kjer so kluči imena, slovar pa vrne prebivalstvo.
    Funkcija vrne slovar"""
    države_file = requests.get("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population").text
    vzorec = r'title=".*?">((?:\w| )*?)</a>.*?\n</td>\n<td style="text-align:right">(.*?)</td>'
    slovar_prebivalstva = {}
    for j in re.finditer(vzorec, države_file):
        slovar_prebivalstva[j.group(1)] = j.group(2)
    # Pri uporabi smo ugotovili, da zaradi tega, ker sta Kraljevina Nizozemska in Nizozemska dve različni entiteti,
    # pride drugače pri kombinirani uporabi te s prejšnjo funkcijo do napake.
    slovar_prebivalstva["Kingdom of the Netherlands"] = slovar_prebivalstva["Netherlands"]
    return slovar_prebivalstva
def obratna_vrednost_prebivalstva(niz_število,tabela_1,tabela_2,tabela_3):
    """Sprejme  število, ki predstavlja državo in vrne nasprotno vrednost prebivalstva.

    Funkcija sprejme število (v obliki niza), ki predstavlja državo in z uporabo slovarjev, ki so definirani v datoteki Države.py
    za vsako število vrne reciprikal prebivalstva države
    tabela_1,tabela_2,tabela_3 predstavljajo tabela_iz_števil_v_kode(), wikipedia_države_in_kode() in wikipedia_populacija()
    a so zaradi optimizacijskih razlgov parametri funkcije in niso v funkciji"""
    prebivalstvo = tabela_3.get(tabela_2.get(tabela_1.get(niz_število,"Ni znano"),"Ni znano"),"Ni znano")
    prebivalstvo_število = prebivalstvo.replace(",","")
    return (lambda x: x if x == "Ni znano" else 1/float(x))(prebivalstvo_število)


def celine():
    """Sprejme številko, ki predstavlja državo in vrne celino.

    Funkcija iz datoteke "country-and-continent-codes-list-csv.csv", ki smo jo našli na 
    https://gist.github.com/stevewithington/20a69c0b6d2ff846ea5d35e5fc47f26c, pobere za vsako državo njeno alpha-2  kodo in celino
    v kateri leži. Iz teh dveh podatkov naredi slovar, ki ga tudi vrne."""
    i = 0
    celine = {}
    vzorec_celine = r'(.*?),([A-Z][A-Z]),(.*?),([A-Z][A-Z]),([A-Z][A-Z][A-Z])'
    with open("csv_datoteke/country-and-continent-codes-list-csv.csv","r") as dat:
        for line in dat:
            if i == 1:
                if re.search(vzorec_celine,line) == None:
                    continue
                else:
                    celine[re.search(vzorec_celine,line).group(4)] = re.search(vzorec_celine,line).group(1)
            elif i == 0:
                i = 1
    return celine
