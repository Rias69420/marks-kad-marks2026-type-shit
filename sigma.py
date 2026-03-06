import json

# Nu mes nolasam tos hujavata datus ble
with open("nuja.json", 'r', encoding="utf-8") as jsonfile: 
    nuja = json.load(jsonfile)

    for prece in nuja:
        print(prece)

        #print(nuja) vnk printe nuja.json lol

# Kipa kk jauni datu ig

es_to_neatbalstu = [
    {"Tips": "Klaviatūra", "Razotajs": "Logitech", "Cena(EUR)": 5},
    {"Tips": "Pele", "Razotajs": "Logitech", "Cena(EUR)": 7}
]

nuja.extend(es_to_neatbalstu)

# with open("nuja.json", 'w', encoding="utf-8") as jsonfile:
#     json.dump(nuja, jsonfile, indent=4, ensure_ascii=False)

new_sigma_input = input("Ievadi sigmu(tips,ražotājs, cena): ").split(',')

new_alpha = {
    "Tips": new_sigma_input[0],
    "Ražotājs": new_sigma_input[1],
    "Cena(EUR)": int(new_sigma_input[2])
}

nuja.append(new_alpha)

print(nuja)

with open("nuja.json", 'w', encoding="utf-8") as jsonfile: 
    json.dump(nuja, jsonfile, indent=4, ensure_ascii=False)

print("Tava ievadītā prece ir veiksmīgi pievienota twin, keep cooking")
