import requests
import re
def wikipedia_države_in_kode():
    države_file = requests.get("https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes").text
    vzorec = r' title="(.*?)">.*?</a>.*?\n</td>\n<td>.*?\n</td>\n<td><a href="/wiki/ISO_3166-1_alpha-2\#([A-Z][A-Z])" title="ISO 3166-1 alpha-2"><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r886049734" /><span class="monospaced">[A-Z][A-Z]</span></a>\n</td>\n<td><a href="/wiki/ISO_3166-1_alpha-3#([A-Z][A-Z][A-Z])" title="ISO 3166-1 alpha-3"><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r886049734" /><span class="monospaced">[A-Z][A-Z][A-Z]</span></a>\n</td>'
    mnoga = {}
    for j in re.finditer(vzorec,države_file):
          mnoga[j.group(2)] = (j.group(1))
    return(mnoga)
print(wikipedia_države_in_kode())