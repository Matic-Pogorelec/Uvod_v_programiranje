import requests
import re
besedilo = requests.get("https://www.chess.com/leaderboard/live/rapid").text
tabela_vzorec = r'countries: \[(.*?)\],'
tabela = re.search(tabela_vzorec,besedilo).group(1)
države = {}
države_preobrat = {}
vzorec = r'{"id":(\d*),"code":"([^"]*)","name":"([^"]*)"}'
for država in re.finditer(vzorec, tabela):
    države[država.group(1)] = [država.group(2),država.group(3)]
    države_preobrat[država.group(2)] = [država.group(1),država.group(3)]
#print(države)
#print(države_preobrat)
i = 0
celine = {}
vzorec_celine = r'(.*?),([A-Z][A-Z]),(.*?),([A-Z][A-Z]),'
with open("country-and-continent-codes-list-csv.csv","r") as dat:
    for line in dat:
        if i == 1:
            if re.search(vzorec_celine,line) == None:
                print(line)
            else:
                celine[re.search(vzorec_celine,line).group(4)] = [re.search(vzorec_celine,line).group(3),re.search(vzorec_celine,line).group(1)]
        elif i == 0:
            i = 1
print(celine)