"""
Tehtävä 4.4
Miika Toivanen
miika.toivanen@edu.sasky.fi


Tee ohjelma, joka tulostaa kaikki sanat lauseesta: "Non scholae sed vitae discimus".

Lisää ominaisuus, jossa ohjelma ilmoittaa, kuinka monta sanaa lauseessa on.

- Muista lisätä koodin kommentit jotka selittävät mitä ohjelma tekee.
"""

def main():
    lause = "Non scholae sed vitae discimus"

    # tulosta lause
    print(lause)

    # sananojen lukumäärä lauseessa
    # string.split() metodi palauttaa kaikki sanat listaan
    # len() funktio palauttaa listan pituuden
    print("Sanojen määrä lauseessa", "\""+lause + "\":", len(lause.split()))


if __name__ == "__main__":
    main()