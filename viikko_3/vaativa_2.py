"""
Viikko 3 vaativa tehtävä 2
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

# Laajenna edellistä ohjelmaa niin, että ohjelma pyytää ensin luvun, joka käyttäjän pitää arvata ja sen jälkeen käyttäjän saa yhteensä viisi yritystä arvata luvun.

from random import randint 


def main():
    print("Arvaa oikea luku!")
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