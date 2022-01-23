"""
Tehtävä 4.4
Tee ohjelma, joka tulostaa kaikki sanat lauseesta: "Non scholae sed vitae discimus".

Lisää ominaisuus, jossa ohjelma ilmoittaa, kuinka monta sanaa lauseessa on.

- Muista lisätä koodin kommentit jotka selittävät mitä ohjelma tekee.
"""

def main():
    lause = "Non scholae sed vitae discimus"

    # tulosta lause
    print(lause)

    # sananojen lukumäärä lauseessa
    # string.split() metodi palauttaa kaikki sanat listaann
    # len() funktio palauttaa listan pituuden
    print("sanojen määrä lauseessa", "\""+lause + "\":", len(lause.split()))


if __name__ == "__main__":
    main()