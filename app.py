from bs4 import BeautifulSoup
import requests

link = 'https://jadwalsholat.org/jadwal-sholat/monthly.php?id=307'

page = requests.get(link)
soup = BeautifulSoup(page.text, 'html.parser')
data = soup.find_all('tr', 'table_highlight')
data = data[0]
print(data)

sholat = {}

i = 0
for d in data:
    if i == 1:
        sholat['imsyak'] = d.get_text()
    elif i == 2:
        sholat['subuh'] = d.get_text()
    elif i == 3:
        sholat['terbit'] = d.get_text()
    elif i == 4:
        sholat['dhuha'] = d.get_text()
    elif i == 5:
        sholat['dzuhur'] = d.get_text()
    elif i == 6:
        sholat['ashar'] = d.get_text()
    elif i == 7:
        sholat['magrib'] = d.get_text()
    elif i == 8:
        sholat['isya'] = d.get_text()
    i += 1

print(sholat)
