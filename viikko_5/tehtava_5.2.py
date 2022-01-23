"""
Tehtävä 5.2


Tee seuraava ohjelma while-silmukalla hyödyntäen .append()-metodia.
Ohjelma kysyy käyttäjältä syntymäpäivää ja lisää sen listaan. Seuraavaksi ohjelma kysyy uutta syntymäpäivää ja lisää sen listaan. Ohjelma kysyy syntymäpäivä, kunnes käyttäjä syöttää l-kirjaimen = lopeta. Lopussa ohjelma tulostaa syntymäpäivälistan.

Esimerkkiajo:

Syötä syntymäpäivä: 11.12.2001
Syötä syntymäpäivä: 1.3.2003
Syötä syntymäpäivä: 20.5.1999
Syötä syntymäpäivä: l

Syötit seuraavat syntymäpäivät:

11.12.2001
1.3.2003
20.5.1999

Kiitos ohjelman käytöstä.

- Muista lisätä koodin kommentit jotka selittävät mitä ohjelma tekee.
"""


def main():
    # syntymäpäivälista
    syntymapaivat = []

    # while-silmukka, kysyy sp:ä kunnes arvoksi annetaan "l"
    while True:
        sp = input("Syötä syntymäpäivä: ")

        # jos arvo on "l", hyppää ulos while silmukasta
        if sp == "l":
            break
        
        # lisää arvon syntymäpäivät listaan
        syntymapaivat.append(sp)

    print("\nSyötit seuraavat syntymäpäivät:\n")

    # tulosta syntymäpäivälistan
    for sp in syntymapaivat:
        print(sp)

    print("\nKiitos ohjelman käytöstä.")


if __name__ == "__main__":
    main()