import random

imena = ['Ivan', 'Antonio', 'Antonija', 'Anto', 'Marijan', 'Zvjezdan', 'Ivan',
       'Mihaela', 'Ružica', 'Dorijan', 'Petra', 'Matej', 'Filip', 'Magdalena',
       'Mate', 'Iva', 'Danis', 'Josip', 'Nebojša', 'Ante', 'Luka', 'Ante',
       'Lorena', 'Ivan', 'Nikola', 'Ivan', 'Helena', 'Ivan', 'Gabrijela',
       'Andrija', 'Regina', 'Petar', 'Dino', 'Marija', 'Semir', 'Gabriela',
       'Borna', 'Filip', 'Krešimir', 'Ivana', 'Gabrijel', 'Vinko', 'Vinko',
       'Romana', 'Viktorija', 'Mija', 'Matej', 'Vinko', 'Luka', 'Antea', 'Ivan',
       'Ivan', 'Luka', 'Daniel', 'Nikola', 'Marko']

ucenici = dict()

for i in imena:
    ucenici[i] = random.randint(1,5)
print("Popis ucenika: ", ucenici)

broj_ocjena = dict()
for ocjena in ucenici.values():
    if ocjena in broj_ocjena:
        broj_ocjena[ocjena] += 1
    else:
        broj_ocjena[ocjena] = 1
print("Broj ocjena: ", broj_ocjena)

broj_ucenika=len(ucenici)
print("Broj ucenika: ", broj_ucenika)

zbroj=0
for ocjena in ucenici.values():
    if ocjena > 1:
        zbroj += 1
print("Zbroj ocjena: ", zbroj)

postotak=(zbroj/broj_ucenika)*100
print("Postotak prolaznosti: ",round(postotak,2),"%")

