# 2. Tehtävä:

# Tee ohjelma, joka pyytää käyttäjältä luvun ja selvittää, onko se parillinen vai pariton. Hyödynnä tarkistuksessa funktiota ja jakojäännöstä.

def main():
    luku = input("Syötä kokonaisluku: ")

    # t3 toinen luku
    luku2 = input("Syötä toinen kokonaisluku: ")

    # tarkista että käytetään numeroa
    if not(luku.isdigit()) and not(luku2.isdigit()):
        print("Ole hyvä ja käytä numeroita.")
        return

    # muuttaa lukuarvon float muotoon
    luku = int(luku)
    luku2= int(luku2) 

    # tarkista onko luku parillinen vai ei
    if luku % 2 == 0:
        print("Syöttämäsi ensimmäinen luku on parillinen.")
    else:
        print("Syöttämäsi ensimmäinen luku on pariton")

    # vertaile kahta lukuarvoa
    if luku > luku2:
        print("1. luku on suurempi kuin 2. luku.")
    elif luku == luku2:
        print("1. luku ja 2. luku ovat samansuuruiset.")
    else:
        print("1. luku on pienempi kuin 2. luku.")


if __name__ == "__main__":
    main()


# 3. Tehtävä:

# Lisää edellisen tehtävän ohjelmaan toiminnallisuus, jossa käyttäjältä kysytään myös toinen luku. Lopuksi ohjelma ilmoittaa, onko ensimmäinen luku parillinen tai pariton sekä vertaa onko ensimmäinen luku isompi, pienempi tai samansuuruinen kuin toinen luku.