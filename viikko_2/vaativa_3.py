"""
Viikko 2 vaativa tehtävä 3
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

# Lisää edellisen tehtävän ohjelmaan toiminnallisuus, jossa käyttäjältä kysytään myös toinen luku. Lopuksi ohjelma ilmoittaa, onko ensimmäinen luku parillinen tai pariton sekä vertaa onko ensimmäinen luku isompi, pienempi tai samansuuruinen kuin toinen luku.


def onko_parillinen(arvo: int) -> int:
    # palauttaa boolean arvon (True tai False) riippuen jakojäännöksestä
    return arvo % 2 == 0


def main():
    # syötä arvo luku-muuttujalle
    luku = input("Syötä kokonaisluku: ")
    
    # tarkista että käytetään kokonaislukua isidigt() metodilla
    if not(luku.isdigit()):
        print("Ole hyvä ja käytä kokonaislukua.")
        return

    # muuttaa lukuarvon INT muotoon
    luku = int(luku)

    # tarkista onko luku parillinen vai ei
    if onko_parillinen(luku):
        print("Syöttämäsi luku on parillinen.")
    else:
        print("Syöttämäsi luku on pariton")


    # syötä arvo (tehtävä 3)
    luku2 = input("Syötä toinen kokonaisluku: ")

    # tarkista että käytetään kokonaislukua isidigt() metodilla
    if not(luku2.isdigit()):
        print("Ole hyvä ja käytä kokonaislukua.")
        return


    luku2 = int(luku2) 

    # vertaile kahta lukuarvoa
    if luku > luku2:
        print("1. luku on suurempi kuin 2. luku.")
    elif luku == luku2:
        print("1. luku ja 2. luku ovat samansuuruiset.")
    else:
        print("Ensimmäinen luku on pienempi kuin toinen luku.")


if __name__ == "__main__":
    main()