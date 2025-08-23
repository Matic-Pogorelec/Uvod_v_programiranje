import numpy as np
import scipy
import pandas as pd
def polinom_ki_gre_skozi_dane_datume(seznam_1,seznam_2):
    """Pomožna funkcija za regresijsko premic za ograf pri analizi, računanje regresijske premice

    Radi bi uporabili np.plyfit, to je funkcija ki izračuna regresijsko premico,  na podatkih, ko je eden tip podatkov datumi
    Vsak datum zamenjamo z številom dni od dneva 2000-01-01 in izračunamo regresijo na teh podatkih
    funkcija vrne urejen par, kjer je prva komponenta seznam slik datumov glede na regresijko premico, druga pa koeficient korelacije"""
    seznam = []
    for i, datum in enumerate(seznam_1):
      seznam.append((datum-np.datetime64("2000-01-01"))/(np.timedelta64(1, 'D')))
    z = np.polyfit(x=seznam, y=seznam_2, deg=1)
    p = np.poly1d(z)
    r = scipy.stats.pearsonr(seznam, seznam_2).statistic
    return (p(seznam),r)


def spremeni_tip_datuma(datum_v_besedni_obliki):
    """Funkija sprejme datum v obliki Aug 27, 2015 in ga pretvori v obliko 2015-08-27."""
    datum_1 = (datum_v_besedni_obliki.split())
    datum_1[1] = datum_1[1][:-1]
    if len(datum_1[1]) == 1:
        datum_1[1] = "0" + datum_1[1]
    koledar = {"Jan": "01",  "Feb": "02", "Mar": "03", 
    "Apr": "04", "May": "05", "Jun":"06", 
    "Jul": "07","Aug": "08", "Sep": "09", 
    "Oct": "10", "Nov":"11", "Dec":"12"}
    return datum_1[2]  +"-" + koledar[datum_1[0]] + '-' + datum_1[1]

def seštej_vse_do_nekega_datuma(tabela):
    """Pomožna funkcija za graf, kjer rišemo število pridruženih šahistov ob nekem času.

    Funkcija ob vsakem datumu izračuna za vsako celino koliko je bilo šahistov iz tiste celino ob tistem datumu.
    Vrne razpredelnico ki ima za index datume, stolpci so pa celine, vrednosti pa to kar smo prej opisali."""
    celine = ["Europe","North America", "South America", "Asia", "Africa", "Oceania"]
    tabela_tabel = [[],[],[],[],[],[]]
    datumi = sorted(list(set(tabela["Datum"])))
    for datum in datumi:
        for i in range(6):
            tabela_tabel[i].append(tabela[(tabela["Celina"] == celine[i]) & (tabela["Datum"] <= datum)].shape[0])
    slovar = {"Europe": tabela_tabel[0], "North America": tabela_tabel[1], "South America": tabela_tabel[2],
    "Asia": tabela_tabel[3], "Africa": tabela_tabel[4], "Oceania": tabela_tabel[5]}
    številski_datumi = list(map(lambda x: np.datetime64(x),datumi))
    return pd.DataFrame(slovar,index=številski_datumi)