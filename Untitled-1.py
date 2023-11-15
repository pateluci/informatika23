import requests
from bs4 import BeautifulSoup

def otevri_odkaz (odkaz):
    response = requests.get(odkaz)
   
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string
    print(f"{title}")


base_url = "https://www.zoopraha.cz/zvirata-a-expozice/lexikon-zvirat?d="


for i in range(1, 10000000000000000000000000000):
    odkaz = f"{base_url}{i}"
    otevri_odkaz(odkaz)

seznam = "odkaz"

# Rozdělí seznam na řádky
radky = seznam.split('\n')

# Projde každý řádek a vypíše části bez '- lexikon zvířat'
for radek in radky:
    casti = radek.split(' - ')
    if len(casti) > 1 and casti[1] == 'lexikon zvířat':
        print(casti[0])
