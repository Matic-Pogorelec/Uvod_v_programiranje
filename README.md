# Analiza chess.com

Naloga je projektno delo pri predmetu Uvod v programiranje. Tema naloge je analiza spletne strani chess.com.
## Uvod
Spletna stran chess.com je najpopularnejša spletna stran za igranje šaha. Poveže te z igralci s celega sveta, da lahko odigraš z njimi partijo. Za vsako odigrano igro dobiš ali izgubiš nekaj točk imenovanih elo na podlagi tega, če si zmagal, remiziral ali izgubil. V nalogi bomo analizirali 1500 igralcev, ki imajo najvišji elo v kategoriji pospešeno, imenovana tudi hitropotezni šah. 

## Struktura analize
Podatke o šahistih bomo analizirali glede na naslednje kategorije
* Analiza po državah

   Šahiste bomo analizirali glede na državo in celino s katere so. Med drugim bomo pogledali kdo so najboljši šahisti v dani državi in katere države so najboljše v šahu
* Analiza po času

   Pogledali si bomo kdaj so se šahisti pridružili na chess.com, kateri izmed njih so najdlje na spletni strani in če so tisti, ki so dlje na spletni strani v povprečju boljši
* Analiza po spolu

   Pogledali si bomo koliko šahistov je moških in koliko žensk, ter kateri so v povprečju boljši.
* Analiza po ogledih

   Analizirali bomo, kateri izmed šahistov so najbolj popularni ter si pogledali za določene države, kdo so najbolj po pularni šahisti v njih. Pogledali si bomo, če obstaja korelacija med elotom in ogledi.
* Ostala analiza

   Ta oddelek bo pa za stvari, ki jih ne moremo lepo vztaviti v nobeno od prej omenjenih kategorij. Pogledali si bomo če obstaja korelacija med številom odigranih iger in, kdo so najbolj po pularni šahisti v njih. Prav tako bomo pogledali, če obstaja korelacija med elotom in ogledi. Del ostale analize je v drugi datoteki. 
## Dokumenti
Projekt vključuje sledeče dokumente

Uvod_v_programiranje
\
&nbsp;&nbsp;**README.md**
\
&nbsp;&nbsp;**main.py**
\
&nbsp;&nbsp;**license**
\
&nbsp;&nbsp;**analiza.ipynb**
\
&nbsp;&nbsp;**analiza_elo.ipynb**
\
&nbsp;&nbsp;pomožne_python_datoteke
\
&nbsp;&nbsp;&nbsp;&nbsp;**manjše_funkcije.py**
\
&nbsp;&nbsp;&nbsp;&nbsp;**čas.py**
\
&nbsp;&nbsp;&nbsp;&nbsp;**osnovna_obdelava**
\
&nbsp;&nbsp;&nbsp;&nbsp;**države_funkcije**
\
&nbsp;&nbsp;csv_datoteke
\
&nbsp;&nbsp;&nbsp;&nbsp;**Glavna_tabela.csv**
\
&nbsp;&nbsp;&nbsp;&nbsp;**country-and-continent-codes-list-csv.csv**
## Uporaba
Bralec mora imeti naložene knjižnice, ki so zapisane v razdelku [Knjižnice in podobne zadeve](#knjižnice-in-podobne-zadeve). Datoteko, ki jo bralec naloži z Githuba je potrebno odpreti znotraj VS Code. Zatem je potrebno pognati datoteko main.py. Zbiranje podatkov traja približno pol ure, v tem času bralec ne rabi biti prisoten.Ta korak pravzaprav sploh ni potreben, saj so podatki že zbrani v Glavna_tabela.csv, a so le ti stari, tako da, če bralec želi ažurne podatke, bo potrebno pognati main.py. Ko so podatki zbrani, je potrebno odpreti datoteko analiza.ipynb. Včasih Jupyter Notebook ne zazna takoj posodobitve dokumenta Glavna_tabela.csv. Po izkušnjah pomaga zapreti in povno odpreti VS Code. Vrstni red poganjanja celic v Jupyter Notebooku ni važen,  v razpotrebno je le začeti s prvo celico. Po končanem branju datoteke analiza.ipynb bo potrebno odpreti še datoteko analiza_elo.ipynb, a bo bralec o tem opomnjen na koncu datoteke analiza.ipynb.
## Knjižnice in podobne zadeve
Potrebno si je naložiti:
* [Pandas](https://pandas.pydata.org/docs/getting_started/install.html)
* [Numpy](https://numpy.org/install/)
* [Jupyter Notebook](https://pypi.org/project/jupyter/)
* [Matplotlib](https://matplotlib.org/stable/install/index.html)
* [Gender guessser](https://pypi.org/project/gender-guesser/)
* [Requests](https://pypi.org/project/requests/)
* [Scipy](https://scipy.org/install/)
* [ipympl](https://matplotlib.org/ipympl/)

