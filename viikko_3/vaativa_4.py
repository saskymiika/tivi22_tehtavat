"""
Viikko 3 vaativa tehtävä 4
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

# Laajenna vielä edellistä ohjelmaa siten, että se kysyy, montako arvauskertaa käyttäjälle annetaan. Jos käyttäjä arvaa oikean luvun kertojen sisällä, onnittele häntä, ja ilmoita, montako arvausta jäi käyttämättä. Tällä kertaa ohjelma näyttää arvausten alussa niiden jäljellä olevan määrän.

from curses import noecho
from random import randint 


def main():
    print("Arvaa oikea luku!")
    lukualue = [None, None]

    print("\nValitse lukualue, jonka väliltä arvattava luku otetaan")

    # listan null checkeri
    def check_nones(list):
        for l in list:
            if l == None:
                return True
        return False

    # hyppää ulos silmuasta kun lukualueeseen on lisätty 2 arvoa
    while check_nones(lukualue):
        # jos aloituslukua ei ole syötetty
        if lukualue[0] == None:
            luku1 = input("\nLuvusta: ")

            # jos luku1 ei ole kokonaisluku
            if not luku1.isdigit():
                print("Syötä kokonaisluku!")
                # hyppää silmukan alkuun
                continue
            # jos on kokonaisluku, lisää lukualueeseen
            lukualue[0] = int(luku1)
        
        # jos lopetuslukua ei ole syötetty
        if lukualue[1] == None:
            luku2 = input("Lukuun: ")

            # jos ei ole kokonaisluku
            if not luku2.isdigit():
                print("Syötä kokonailuku!")
                # hyppää silmukan alkuun
                continue
            # jos on kokonaisluku, lisää...
            lukualue[1] = int(luku2)


    # valitse luku satunnaisesti 1 - 100 väliltä
    luku = randint(lukualue[0], lukualue[1])

    # yrityksiä muuttuja
    arvauksia = ""
    visual_arvauksia = []

    # tulostaa arvausten määrät
    def print_visual_list(list):
        index = len(list) - arvauksia
        for x in range(index):
            if list[x] != "#":
                list[x] = "#"
        print("\n["+("|".join(list))+"]")


    # kysy arvausten määrää
    while True:
        arvauksia = input("\nKuinka monta arvauskertaa sallitaan? ")
        if arvauksia.isdigit():
            # muuta arvauksia muutuja kokonaisluvuksi ja hyppää ulos...
            arvauksia = int(arvauksia)
            # lisää visaul listaan arvauskerrat
            for x in range(arvauksia):
                visual_arvauksia.append('_')
            break
        else:
            print('Syötä kokonaisluku!')


    while True:
        # jos yrityksiä on alle 1, lopeta ohjelma
        if arvauksia < 1:
            print("\nEt arvannut oikeaa lukua. Oikea luku oli:", luku)
            break

        # tulosta yrityksiä jäljellä
        print_visual_list(visual_arvauksia)
        print("Sinulla on "+str(arvauksia)+"/"+str(len(visual_arvauksia))+" yritystä jäljellä")

        # kysy lukua
        arvaus = input("\nSyötä luku "+str(lukualue[0])+" - "+str(lukualue[1])+" väliltä.\nLukusi: ")

        # tarkista että syötetty arvo on kokonaisluku
        if arvaus.isdigit():
            # vertaa arvausta annettuu lukuu
            if int(arvaus) < luku:
                print("Lukusi on liian PIENI.")
            elif int(arvaus) > luku:
                print("Lukusi on liian SUURI.")
            else:
                print("\nHienoa! Arvasit oikein!", "Arvauksia jäi jäljelle:", arvauksia)
                print("\nKiitos ohjelman käytöstä.")
                break

            # vähennä yrityksiä
            arvauksia -= 1
        else:
            print("\nOle hyvä ja käytä kokonaislukua.")


if __name__ == "__main__":
    main()