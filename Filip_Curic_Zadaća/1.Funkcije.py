ime = input("Unesi ime: ")
def pozdrav(ime):
    return "Pozdrav " + ime

dobrodosao = lambda ime: "Dobrodošao " + ime + "!"

def ispisi_poruku(funkcija):
    print(funkcija(ime))

ispisi_poruku(pozdrav)
ispisi_poruku(dobrodosao)
