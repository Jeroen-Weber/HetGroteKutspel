######################
# HET GROTE KUT SPEL #
# Copy Jeroen Weber  #
######################
# Project op Github te vinden op: https://github.com/Jeroen-Weber/HetGroteTMspel
# -*- coding: utf-8 -*-

# een aantal imports om bepaalde functie's en variabele  te laten werken
import webbrowser
import time
from colorama import Fore

# een leuk kleurtje voor de STOP zin
kleur = "BLUE"

# ERRORS en Prints alvast vast leggen om onnodige prints te voorkomen  en moeite te besparen.
spel_STOP = "Okay, bedankt voor het spelen! Het spelletje is gedaan (c) Jeroen Weber Student @ Thomas More"
jammer = "Hahah dat is nou eens jammerv"
goed_gedaan = "Dat heb je goed gedaan! Het spel is trots op je! Jahoor."
extra_uitleg = "TER INFO: Alles werkt om het spel te starten, behalve nee of iets waar dat op lijkt."
pedo_zin = "Pas wel op he, met minder jarige meisjes, kan je problemen mee krijgen. Ze doen er soms moeilijk om , maar je weet hoe dichter bij de 0.. hoe strakker om de lul"
leeftijds_verschil = "Er zit wel groot leeftijdsverschil tussen jullie. Maar boeie ruud"
verkracht_vriendin = "Weet je zeker dat je niet verkracht word door je vriendin? :P"
ja_gedaan = "Dat is wel lekker hoor, zeker wel gemist? Heb je het wel een beetje goed opgeruimd? Anders ziet je mama dat ;p en dat willen we niet!"


# FUNCTIE Tinder
def tinder():
    bestand_tinder = open("tinder.txt")
    print(bestand_tinder.read())
    bestand_tinder.close()


# einde Functie Tinder

# FUNCTIE: Pedochecker

def pedochecker():
    if int(leeftijd) >= 18 and leeftijd_meisje <= 16:
        print(pedo_zin)
        print("https://nl.wikipedia.org/wiki/Verkrachting")
    elif int(leeftijd) - leeftijd_meisje >= 5 or leeftijd_meisje - int(leeftijd) >= 5:
        print(leeftijds_verschil)
    elif int(leeftijd) < 18 <= leeftijd_meisje:
        print(verkracht_vriendin)


# einde funcie pedochecker

# FUNCTIE: vriendje/vriendin
def vriendin_vriendje():
    """Dit checkt of je een vriendje of een vriendin hebt, nagelang je geslacht."""
    if jongen_meisje == "jongen":
        print("vriendinnen")
    if jongen_meisje == "meisje":
        print("vriendjes")
    print()


# Einde Functie vriendje/vriendin


# FUNCTIE: No Not November


def nnn():
    """Progamma van No-Nut-November, deze checkt of je dat hebt overleefd, en hoe leuk je de challange vond. En print dan al je antwoorden"""

    print(jammer)
    NNN = input(
        "Hahaha, wat een maagd dat je bent, heb je nog nooit mogen prikken.. Heb je no not november overleeft? ").strip()
    print("")
    if NNN == "ja":
        print(goed_gedaan)
        gedaan = input("Heb je het in december al gedaan? ").strip()
        print("")
        if gedaan == "ja":
            print(ja_gedaan)
    else:
        lekker = input("Gast slecht dat je bent, was het  wel lekker? ").strip()
        print("")
        if lekker == "ja":
            print('Lekker man , genieten is dat hoor. Heb je leuke video gevonden om jezelf te helpen? ')
            videos = input("Wil je een lijst hebben met goede website's in je mail? ").strip()
            if videos == "ja":
                print("Helaas dat kan ik nog niet progammeren.")
                print(Fore.BLUE + spel_STOP)
        if lekker == "nee":
            print("Hier heb je een aantal super goede website's ")

            # open bestand met alle porno site's en write nieuwe en user er 1 weet
            pornsites = open('pornsites.txt', 'r+')
            print(pornsites.read())
            print("Weet je misschien nog een leuke site? jij viezerik! Kan je hieronder invullen..")
            site = input("Naam van de website: ")
            pornsites.write(site + "\n")
            pornsites.close()

            time.sleep(2)
            if site == "nee":
                print("SAAAAAAAAAAIIII")
            else:
                print("Bedankt, viezerik. Het is aan het lijstje toegevoegd.")

    return Fore.BLUE + spel_STOP


# EINDE Functie NNN


# De titel en de spelregels laden in een apart bestand om overbodige prints te voorkomen.
bestand = open("Hoofdprogamma_OPENING.txt")
print(bestand.read())
bestand.close()

# spatie
print("")

# vragen of de gebruiker klaar is om het spel te starten.
print(extra_uitleg)
spel_begin = input("Heb je de spelregels gelezen en ben je klaar om met het spel te beginnen? ")

# de input verlagen naar kleine letters
spel_begin = spel_begin.lower()

# spatie
print("")

# als de gebruiker nee zegt, of iets wat daar op lijkt. stopt het spel, en krijgt ook een video te zien over bij je moeder huilen :P
if "nee" in spel_begin or "nop" in spel_begin or "nehh" in spel_begin or "neee" in spel_begin or "ne" in spel_begin:
    print("Okay, fijn dat je het aangeeft. MIETJE. Ga lekker bij je mama huilen.")
    stop = 1
    time.sleep(1)
    print("https://www.youtube.com/watch?v=9cRiNplRH2g")
    webbrowser.open('https://www.youtube.com/watch?v=9cRiNplRH2g')

# als de gebruiker iets anders ingeeft. begint het spel.
else:
    # nog even checken of de input niet belachelijk lang is.
    if len(spel_begin) > 3:
        print(
            "Vul alsjeblieft bij de volgende vragen iets fatsoenlijks in, het spel is niet gedaan maar niet te enthousiast doen he :P")

    # standaard informatie vragen zoals naam en leeftijd
    naam = input("Simpele vraag, om te beginnen: Wat is je voor en achternaam? ").strip()
    split = naam.split(" ", 1)
    voornaam = split[0]
    leeftijd = input("Wat is je leeftijd, " + voornaam + "? ").strip()

    # eerst, kijken of je wel een int hebt ingevuld bij de leeftijd en een str bij de naam
    if naam.isdigit():
        print("Gast, sinds wanneer heb je als een naam een getal? SPEEL NORMAAL!")
        naam = input("Wat is je echte naam? ").strip()

    if not leeftijd.isdigit():
        print("Wow wacht even... heb je nu dat fout ingevuld, je leeftijd?! kom op zeg.. HOMO")
        leeftijd = int(input("Hoeveel jaar ben je echt? "))

    # vervolgens, kijken dat je niet te jong of te oud bent. zie spelregels.
    if int(leeftijd) < 15:
        print("Sorry, je bent te jong om mee te doen met dit spel.")
        stop = 1
    if int(leeftijd) > 100:
        print("gast, klootzaak. vul even je echte leeftijd in")
        stop = 0
    if int(leeftijd) > 25:
        print("HAHAHA gast, je bent ", leeftijd, "jaar. Ga wat nuttigs doen in je leven.")
        print("Leuk gedicht: 2 neven in een pizza oven!")
        stop = 1
        print(Fore.BLUE + spel_STOP)
    else:
        stop = 0
        # nog even vragen na het geslacht
        jongen_meisje = input(
            "Ben je een jongen, meisje, mongooltje, autist of wil je het niet vertellen? (mietje) ").strip()

        # kijken welk geslacht de speler heeft, en een passend bericht bij geven ALS stop niet 1 is. zie leeftijd checker.
        if "mongool" in jongen_meisje:
            print("Hahahahaha , jajaja even de grapjas uithangen in mijn game he, jajajaaj. We weten allebei dat",
                  jongen_meisje, "geen geslacht is. Dus even normaal doen aub")
            time.sleep(2)
            webbrowser.open('https://pbs.twimg.com/profile_images/1732374435/2dv1icy_400x400.png')

        # spatie
        print("")

        # als je autist invuld
        if "autist" in jongen_meisje:
            print(
                "Ik denk dat je dan even je mama erbij moet halen, dit is een spelletje voor MENSEN MET HERSENENEN!!!!!")
            time.sleep(1)
            print(Fore.BLUE + spel_STOP)
            stop = 1

        # als je niet wilt vertellen
        if "vertellen" in jongen_meisje:
            print("Wat een godverdomme mietje ben jij nou weer. wees een een man en zegt wat je tussen je benen hebt!")
            time.sleep(1)
            print("Okay, vooruit je mag weer verder doen van mij. iedereen verdiend een tweede kans, toch?!")
            stop = 0

        # spatie
        print("")

        if jongen_meisje == "jongen":
            print("hoeveel scharrel(s) heeft '", voornaam, "' al gehad? ")
            geef_in_aantal = int(input("...... Eerlijk zijn, hoeveel (¬‿¬)? "))
            if geef_in_aantal > 4:
                print("Sow! PLAYEEEERRRR SPOTTED... ¬_¬")

        elif jongen_meisje == "meisje":
            print("Welkom", naam, ", hoeveel vriendjes heb je al gehad? ")
            geef_in_aantal = int(input("...... Eerlijk zijn, hoeveel (¬‿¬)? "))
            if geef_in_aantal > 4:
                print("Sow! PLAYEEEERRRR SPOTTED... ¬_¬")

            # extra controle
            if geef_in_aantal > 4:
                print("Sow! PLAYEEEERRRR SPOTTED... ¬_¬")

        # spatie
        print("")

# kijken of de speler geen stop = 1 heeft gekregen, want dan is het spel gestopt, en mag onderstaand niet meer worden uitgevoerd
if not stop == 1:

    # kijken of de speler een vriendin heeft op dit moment.
    momenteel = input("Dus heb je momenteel een scharrel? ")
    momenteel = momenteel.lower()

    # als je momenteel vriendin hebt dan..
    if "ja" in momenteel:

        # informatie over de vriendin
        naam_vriendin = input("Wat is de naam van je vriendin? ")
        print(naam_vriendin, ", dat is een schattige naam. ")
        leeftijd_meisje = int(input("Hoe oud is je vriendin? "))

        # de PEDO-CHECKER: zie functie bovenaan progamma
        pedochecker()

    # als je momenteel geen vriendin hebt RUN de functie tinder
    else:
        tinder()

    # spatie
    print("")

    # extra bericht als eerste vriendin is. ( geef_in_aantal error weet ik = normaal )
    if momenteel == "ja" and geef_in_aantal == 1:
        print("Cute, is dit je eerste relatie? wat schattig. URGH")
        print("")

    # extra bericht als je ouder bent als 21 en dit je eerste vriendin zou zijn.
    if momenteel == "ja" and geef_in_aantal == 1 and int(leeftijd) > 20:
        print("Godverdomme is dit je eerste vriendin? Wtf hahahaha werd tijd jonguh ")

    # seks checker voor de volgende vragen
    seks = input("Heb je ooit seks gehad? ").lower()

    # kijken of seks goed is ingevuld
    if not seks == "nee" and not seks == "ja":
        print("vul alsjeblieft gewoon even ja of nee in..")
        seks = input("Dus.. heb je ooit seks gehad? ").lower()

    # als je nog geen vriendinnetjes hebt gehad
    if geef_in_aantal == "0":

        # als je nog geen seks hebt gehad
        if seks != "nee":
            print("Owh wat een gelukzak dat je bent! Was ze blind dan of?")

        # als je wel seks hebt gehad, of iets waar dat op lijkt
        else:
            print(nnn())

    # als je geen vriendinnetjes hebt gehad dan run je dit
    else:

        # checken wat antwoord was op de seks vraag
        if "nee" in spel_begin or "nop" in spel_begin or "nehh" in spel_begin or "neee" in spel_begin or "ne" in seks:
            print(nnn())

        # vragen als het antwoord ja (of iets anders) was op de seks vraag
        else:
            condoom = input("Dat is wel erg lekker , wel met condoom hoop ik voor je? ").strip().lower()
            print("")

            # als je condoom hebt gebruikt
            if "ja" in spel_begin or "jha" in spel_begin in condoom:
                print("Goedzo! geen kindjes voor jou! Knan je nog even genieten van je luxe leventje!")
                print(Fore.BLUE + spel_STOP)

            # als er geen condoom word gebruikt...
            else:
                print("Sow dus je wilt vader worden? yes! mini", naam, "tjes!")

                # vragen of de pil word gebruikt
                pil = input("Gebruik je vriendin de pil? ")
                if "ja" in spel_begin or "jha" in spel_begin in pil:
                    print("Gelukkig, dan ga je toch geen kinderen krijgen :) , of wil je wel graag kinderen? neeeh")

                    # leeftijd checker, kijken of kinderen goede leeftijd is
                    if int(leeftijd) >= 21:
                        print(
                            "Opzich kinderen zou wel kunnen, je bent ouder dan 21 opzich mooie leeftijd. NEUKEN!!!!!!!")
                    elif int(leeftijd) <= 16:
                        print("Wow, je bent jonger dan 16, niet echt slim om nu kinderen te nemen... beeeeetje vroeg")
                    elif 21 > int(leeftijd) > 16:
                        print(
                            "Hmmm ja geen idee.. die leeftijd die je hebt ingegeven in het systeem. geen idee of je kinderen op die leeftijd wilt.")

                    print(Fore.BLUE + spel_STOP)

                else:
                    MJ = input("Word het een jongetje of een meisje ;p? m/j ").strip().lower()
                    if MJ == "j":
                        print("Yes kan je samen naar PSV gaan kijken in eindhoven")
                        print(Fore.BLUE + spel_STOP)
                    elif MJ == "m":
                        print("Meisje is ook leuk, niet?")
                        print(Fore.BLUE + spel_STOP)
                    else:
                        print("Wat voor raar monster ga jij maken?")
                        print(Fore.BLUE + spel_STOP)
