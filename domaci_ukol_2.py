import requests

# část 1

ICO = input("Zadej ICO:")
response = requests.get(
    f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ICO}")
data = response.json()

print(data["obchodniJmeno"])
print(data["sidlo"]["textovaAdresa"])

# část 2

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

nazev_subjektu = input("Zadej nazev subjektu:")
data = f'{{"obchodniJmeno": "{nazev_subjektu}"}}'

response = requests.post(
    "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)
data = response.json()

nalezeno_subjektu = data["pocetCelkem"]
subjekty = data["ekonomickeSubjekty"]

print(f"Nalezeno subjektů: {nalezeno_subjektu}")

for subjekt in subjekty:
    obchodni_jmeno = subjekt["obchodniJmeno"]
    ICO = subjekt["ico"]
    print(f"{obchodni_jmeno}, {ICO}")
