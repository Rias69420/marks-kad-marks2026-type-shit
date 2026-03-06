import json

with open("nuja.json", 'r', encoding="utf-8") as jsonfile:
    sluha = json.load(jsonfile)

nu_viss_dargakais = max(sluha, key=lambda x: x.get("Cena(EUR)", 0))

print("Viss dargaka sluha: ")
print(nu_viss_dargakais)