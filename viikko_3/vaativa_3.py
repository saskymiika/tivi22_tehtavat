"""
Viikko 3 vaativa tehtävä 3
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

# Laajenna vielä edellistä ohjelmaa siten, että se kysyy ensin käyttäjältä lukualueen, jolle arvattava numero halutaan sijoittaa. Sen jälkeen ohjelma näyttää alueen ja pyytää valitsemaan luvun alueelta. Viimeiseksi ohjelma pyytää käyttäjää arvaamaan oikean luvun. Käyttäjällä on viisi arvauskertaa käytössään.

from random import randint 


def main():
    print("Arvaa oikea luku!")
    lukualue = [None, None]

    print("\nValitse lukualue, jonka väliltä arvattava luku otetaan")

    # hyppää ulos silmuasta kun lukualueeseen on lisätty 2 arvoa
    while len(lukualue) < 2:
        # jos aloituslukua ei ole syötetty
        if lukualue[0] == None:
            luku1 = input("\n Luvusta: ")

            # jos luku1 ei ole kokonaisluku
            if not luku1.isdigit():
                print("Syötä kokonaisluku!")
                # hyppää silmukan alkuun
                continue
            # jos on kokonaisluku, lisää lukualueeseen
            lukualue.append(int(luku1))
        
        # jos lopetuslukua ei ole syötetty
        if lukualue[1] == None:
            luku2 = input("Lukuun: ")

            # jos ei ole kokonaisluku
            if not luku2.isdigit():
                print("Syötä kokonailuku!")
                # hyppää silmukan alkuun
                continue
            # jos on kokonaisluku, lisää...
            lukualue.append(int(luku2))


    # valitse luku satunnaisesti 1 - 100 väliltä
    luku = randint(1, 100)

    # yrityksiä muuttuja
    yrityksia = 5

    while True:
        # jos yrityksiä on alle 1, lopeta ohjelma
        if yrityksia < 1:
            print("\nEt arvannut oikeaa lukua. Oikea luku oli:", luku)
            break

        # tulosta yrityksiä jäljellä
        print("\nSinulla on "+str(yrityksia)+" yritystä jäljellä")

        # kysy lukua
        arvaus = input("\nSyötä luku 1 - 100 väliltä.\n\nLukusi: ")

        # tarkista että syötetty arvo on kokonaisluku
        if arvaus.isdigit():
            # vertaa arvausta annettuu lukuu
            if int(arvaus) < luku:
                print("\nLukusi on liian PIENI.")
            elif int(arvaus) > luku:
                print("\nLukusi on liian SUURI.")
            else:
                print("\nHienoa! Arvasit oikein!")
                print("\nKiitos ohjelman käytöstä.")
                break

            # vähennä yrityksiä
            yrityksia -= 1
        else:
            print("\nOle hyvä ja käytä kokonaislukua.")


if __name__ == "__main__":
    main()