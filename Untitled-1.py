


import requests

url = "https://www.zoopraha.cz/zvirata-a-expozice/lexikon-zvirat"

response = requests.get(url)

if response.status_code == 200:
    # Tisk obsahu stránky
    print(response.text)
else:
    print(f"Chyba při stažení stránky. Stavový kód: {response.status_code}")
