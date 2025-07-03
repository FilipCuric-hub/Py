rezultati = []

with open('rezultati.csv', 'r', encoding='utf-8') as file:
    for linija in file:
        ime, prezime, bodovi = linija.strip().split(',')
        rezultati.append((ime, prezime, int(bodovi)))

for ime, prezime, bodovi in rezultati:
    if bodovi > 49:
        print(ime, prezime, bodovi)


rezultati.sort(key=lambda x: x[1])

ocjene = {
    "Nedovoljan": 0,
    "Dovoljan": 0,
    "Dobar": 0,
    "Vrlo dobar": 0,
    "Odličan": 0
}

for ime, prezime, bodovi in rezultati:
    if bodovi < 50:
        ocjene["Nedovoljan"] += 1
    elif bodovi < 65:
        ocjene["Dovoljan"] += 1
    elif bodovi < 80:
        ocjene["Dobar"] += 1
    elif bodovi < 90:
        ocjene["Vrlo dobar"] += 1
    else:
        ocjene["Odličan"] += 1


for ocjena in ocjene:
    print(ocjena, ocjene[ocjena])
