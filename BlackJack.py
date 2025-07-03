import pygame
import random
import copy

pygame.init()

#OSNOVNE POSTAVKE-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-
karte = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
spil = 4*karte
dek = 4
#-----------------------------------------------------
WIDTH = 600
HEIGHT = 780
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("BlackJack by Cofi")
fps = 60
timer = pygame.time.Clock()
#----------------------------------------------------
font = pygame.font.Font("freesansbold.ttf", 40)
manji_font = pygame.font.Font("freesansbold.ttf", 30)
active = False
#----------------------------------------------------
rekord = [0, 0, 0]
igrac = 0
diler = 0
#Pocetak igre------------------------------------------
prvo_dijeljenje = False
moja_ruka = []
dilerova_ruka = []
krajnji_rezultat = 0

otkri_diler = False
ruka_aktiv = False

pobjednik = 0
dodaj_rezultat = False

poruke = [" ", "POHLEPAN SI !", "POBJEDA !", "NEDOVOLJAN :(", "NERJESENO"]

#Djeljenje nasumicnih karata(Jednu po jednu)------------------------------
def dijeli_karte(trenutna_ruka, trenutni_dek):
    karta = random.randint(0, len(trenutni_dek))
    trenutna_ruka.append(trenutni_dek[karta-1])
    trenutni_dek.pop(karta-1)
    return trenutna_ruka, trenutni_dek

def stanje_ruku(igrac, diler):
    screen.blit(manji_font.render(f'stanje ruke:[{igrac}]', True, 'white'), (365, 320))
    if otkri_diler:
        screen.blit(manji_font.render(f'stanje ruke:[{diler}]', True, 'white'), (365, 275))


#DIZAJN KARATA---------------------------------------------------------------------
def crtaj_karte(igrac, diler, otkri):
    for i in range (len(igrac)):
        pygame.draw.rect(screen, "white", [70 + (70*i), 360 + (5 +i), 100, 200], 0, 5)
        screen.blit(font.render(igrac[i], True, "black"),(80 + 70*i, 375 + 5*i))
        screen.blit(font.render(igrac[i], True, "black"),(125 + 70*i, 520 + 5*i))
        pygame.draw.rect(screen, "yellow", [70 + (70*i), 360 + (5 +i), 100, 200], 8, 5)

    #Dilerova karte(SAKRIVENE)---------------------------------------------------------
    for i in range (len(diler)):
        pygame.draw.rect(screen, "white", [70 + (70*i), 60 + (5 +i), 100, 200], 0, 5)
        if i != 0 or otkri_diler:
            screen.blit(font.render(diler[i], True, "black"),(80 + 70*i, 75 + 5*i))
            screen.blit(font.render(diler[i], True, "black"),(120 + 70*i, 220 + 5*i))
        else:
            screen.blit(font.render("?", True, "black"),(80 + 70*i, 75 + 5*i))
            screen.blit(font.render("?", True, "black"),(120 + 70*i, 220 + 5*i))
        pygame.draw.rect(screen, "purple", [70 + (70*i), 60 + (5 +i), 100, 200], 8, 5)


#Racunanje ruke------------------------------------------------------
def izracunaj_rezultat(ruka):
    stanje_ruke = 0
    as_brojac = ruka.count("A")
    for i in range(len(ruka)):
        #zbrajaj obicne karte:---------------------------------
        for j in range(8):
            if ruka[i] == karte[j]:
                stanje_ruke += int(ruka[i])
        #zbrajaj 10ke:-----------------------------------------
        if ruka[i] in ["10", "J","Q", "K"]:
            stanje_ruke += 10
        #za AS-a prvo 11 pa poslje 1 ako treba--------------------- 
        elif ruka[i] == "A":
            stanje_ruke += 11
    #konverzija AS-a-------------------------------------------------
    if stanje_ruke > 21 and as_brojac > 0:
        for i in range(as_brojac):
            if stanje_ruke > 21:
                stanje_ruke -= 10
    return stanje_ruke       


#DIZAJN-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-
def dizajn(act, rekord, kraj):
    lista_tipki = []
    
    #U pocetku nije aktivno osim ako ne dijeli karte-----------------------
    if not act:
        podijeli = pygame.draw.rect(screen, "white", [150, 20, 365, 100], 0, 5)
        pygame.draw.rect(screen, "green", [150, 20, 365, 100], 3, 5)
        podijeli_text = font.render("PODIJELI KARTE", True, "black")
        screen.blit(podijeli_text, (165, 50))
        lista_tipki.append(podijeli)

    #Kada su karte podjeljene(HIT, STAND)---------------------------------------
    else:
        hit = pygame.draw.rect(screen, "white", [10, 600, 250, 100], 0, 5)
        pygame.draw.rect(screen, "green", [10, 600, 250, 100], 3, 5)
        hit_text = font.render("NOVA", True, "black")
        screen.blit(hit_text, (75, 630))
        lista_tipki.append(hit)
        
        stand = pygame.draw.rect(screen, "white", [350, 600, 240, 100], 0, 5)
        pygame.draw.rect(screen, "green", [350, 600, 240, 100], 3, 5)
        stand_text = font.render("STANI", True, "black")
        screen.blit(stand_text, (410, 630))
        lista_tipki.append(stand)

        rekord_text = manji_font.render(f"Rekord:  W: {rekord[0]}    L: {rekord[1]}    D: {rekord[2]}", True, "white")
        screen.blit(rekord_text, (0, 740))
        
    #Ako ima kraja:(RESTART, PORUKA)----------------------------------------------------------
    if kraj != 0:
        screen.blit(font.render(poruke[kraj], True, 'gold'), (55, 300))
        podijeli = pygame.draw.rect(screen, "white", [150, 20, 365, 100], 0, 5)
        pygame.draw.rect(screen, "black", [150, 20, 365, 100], 3, 5)
        pygame.draw.rect(screen, "green", [153, 23, 366, 101], 3, 7)
        podijeli_text = font.render("NOVA RUKA", True, 'black')
        screen.blit(podijeli_text, (205, 50))
        lista_tipki.append(podijeli)     
    return lista_tipki

    
#Pregled za KRAJ------------------------------------------------------------------
def provejra_kraja(ruka_aktiv, diler, igrac, kraj, total, dodaj):
    #Igrac stao,prikuco,21--------
    #prikuco(1);pobjeda(2);poraz(3);4-X-----------------------------------------
    if not ruka_aktiv and diler >= 17:
        if igrac > 21:
            kraj = 1
        elif diler < igrac <= 21 or diler > 21:
            kraj = 2
        elif igrac < diler <= 21:
            kraj = 3
        else:
            kraj = 4
        if dodaj:
            if kraj == 1 or kraj == 3:
                total[1] += 1
            elif kraj == 2:
                total[0] += 1
            else:
                total[2] += 1
            dodaj = False
    return kraj, total, dodaj

#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
#GLAVNI DIO IGRE-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
run = True
while run:
    timer.tick(fps)
    screen.fill("red")
    #DJELJENJE------------------------------------------------------------------------------
    if prvo_dijeljenje:
        for i in range(2):
            moja_ruka, dek_igre = dijeli_karte(moja_ruka, dek_igre)
            dilerova_ruka, dek_igre = dijeli_karte(dilerova_ruka, dek_igre)
        prvo_dijeljenje = False
            
    #KADA IGRA POCNE(PRVE PODJELJENE, KALKULATOR)--------------------------------------------
    elif active:
        igrac = izracunaj_rezultat(moja_ruka)
        crtaj_karte(moja_ruka, dilerova_ruka, otkri_diler)
        if otkri_diler:
            diler = izracunaj_rezultat(dilerova_ruka)
            if diler < 17:
                dilerova_ruka, dek_igre = dijeli_karte(dilerova_ruka, dek_igre)
        stanje_ruku(igrac, diler)
    tipke = dizajn(active, rekord, pobjednik)


#IZLAZ/ULAZ IGRE---------------------------------------------------------------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            if not active:
                if tipke[0].collidepoint(event.pos):
                    active = True
                    prvo_dijeljenje = True

                    dek_igre = copy.deepcopy(dek * spil)
                    moja_ruka = []
                    dilerova_ruka = []
                    krajnji_rezultat = 0
                    ruka_aktiv = True
                     
                    pobjednik = 0
                    dodaj_rezultat = True

            else:
                #Ako igrac HOCE, vuci jos----------------------------------------
                if tipke[0].collidepoint(event.pos) and igrac < 21 and ruka_aktiv:
                    moja_ruka, dek_igre = dijeli_karte(moja_ruka, dek_igre)
                #Ako igrac Nece, diler vuce----------------------------------------
                elif tipke[1].collidepoint(event.pos) and not otkri_diler:
                    otkri_diler = True
                    ruka_aktiv = False
                #RESET----------------------------------------------------------
                elif len(tipke) == 3:
                    if tipke[2].collidepoint(event.pos):
                        active = True
                        prvo_dijeljenje = True
                        dek_igre = copy.deepcopy(dek * spil)
                        moja_ruka = []
                        dilerova_ruka = []
                        krajnji_rezultat = 0
                        ruka_aktiv = True
                        pobjednik = 0
                        dodaj_rezultat = True
                        otkri_diler = False
                        diler = 0
                        igrac = 0

    #Ako igrac PRIKUCA, diler vuce(isto ko da nece)---------------------------------
    if ruka_aktiv and igrac >= 21:
        ruka_aktiv = False
        otkri_diler = True

    pobjednik, rekord, dodaj_rezultat = provejra_kraja(ruka_aktiv, diler, igrac, krajnji_rezultat, rekord, dodaj_rezultat)

    pygame.display.flip()
pygame.quit()


    
    

















