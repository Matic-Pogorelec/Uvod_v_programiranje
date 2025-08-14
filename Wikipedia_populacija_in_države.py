import requests
import re
def zlepi(seznam):
    if seznam == []:
        return ""
    else:
        return seznam[0] + zlepi(seznam[1:])
def odstrani_vejice_in_intigiraj(niz):
    return(int(zlepi(niz.split(","))))
def wikipedia_populacija():
    države_file = requests.get("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population").text
    vzorec = r'title=".*?">((?:\w| )*?)</a>.*?\n</td>\n<td style="text-align:right">(.*?)</td>'
    mnoga = {}
    for j in re.finditer(vzorec, države_file):
        mnoga[j.group(1)] = odstrani_vejice_in_intigiraj(j.group(2))
    return mnoga
print(len(wikipedia_populacija()))

