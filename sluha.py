import csv

with open("preces.csv", newline='') as csvfile:
    preces = csv.reader(csvfile)
    next(preces)

    for line in preces:
        print(line)

# Datu rakstīšana no programmas

new_sigma = [ 
    ["Printeris", "HP", "100"],
    ["Skeneris", "Dell", "48.99"]
]

with open("preces.csv", 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # writer.writerows(new_sigma)

# Datur rakstīšana no termināla
    new_sigma = input("Ievadi preci(Tips, Razotajs, Cena): ").split(',')
    writer.writerow(new_sigma)

    