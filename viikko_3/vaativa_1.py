# 1. Tehtävä

# Jatka tehtävää 4.1 ja tee ohjelmaan silmukka, jolla ohjelma kysyy oikeaa numeroa käyttäjältä, kunnes hän arvaa oikein.

# Esimerkkiajo: (oikea luku on määritetty 33)

# Arvaa luku välillä 1 - 100: 23
# Arvaus on liian pieni.

# Arvaa luku väliltä 1 - 100: 55
# Arvaus on liian suuri.

# Arvaa luku väliltä 1 - 100: 45
# Arvaus on liian suuri.

# Arvaa luku väliltä 1 - 100: 35
# Arvaus on liian suuri.

# Arvaa luku väliltä 1 - 100: 30
# Arvaus on liian pieni.

# Arvaa luku väliltä 1 - 100: 32
# Arvaus on liian pieni.

# Arvaa luku väliltä 1 - 100: 33
# Hienoa! Oikea arvaus!

# Kiitos ohjelman käytöstä.

from random import randint 


def main():
    # valitse luku satunnaisesti 1 - 100 väliltä
    luku = randint(1, 100)

    while True:
        # kysy lukua
        arvaus = input("\nArvaa luku väliltä 1 - 100: ")

        # tarkista että syötetty arvo on kokonaisluku
        if arvaus.isdigit():
            # vertaa arvausta annettuu lukuu
            if int(arvaus) < luku:
                print("\nArvaus on liian pieni.")
            elif int(arvaus) > luku:
                print("\nArvaus on liian suuri.")
            else:
                print("\nHienoa! Oikea arvaus!")
                print("\nKiitos ohjelman käytöstä.")
                break
        else:
            print("\nOle hyvä ja käytä kokonaislukua.")


if __name__ == "__main__":
    main()