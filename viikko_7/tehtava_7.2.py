"""
Tehtävä 7.2
Miika Toivanen
miika.toivanen@edu.sasky.fi


Muokkaa aiemmin tehtävässä 5.4 tekemäsi kauppalistaohjelma siten, että valikkorakenteesta kutsutaan funktioita.

Vinkki: Käytä siis aiemmin kirjoittamaasi koodia ja siirrä sitä sopivasti copy/pastella funktioiden sisälle.
"""


def valikko_toiminto():
    while True:
        print("\nValitse toiminto:")
        toiminto = input("1 - Lisää tuote\n2 - Poista syötetty tuote\n3 - Tulosta lista\n4 - Tyhjennä lista\n0 - Lopetus\n\nAnna valintasi: ")

        # tarksitaa että käytetään kokonaislukua ja että pituus on 1
        if toiminto.isdigit() and len(toiminto) == 1:
            # varmista että arvo on pienempi kuin 5 listassa annettujen esimerkkien mukaan
            if int(toiminto) < 5:
                # palauta arvo
                return toiminto

        # jos valinta on väärä, ilmoita siitä ja looppaa uudelleen
        print("Ole hyvä ja syötä 1, 2, 3, 4 tai 0")


# kauppalista parametrille määritetty tyyppi: List
def lisaa_tuote(kauppalista: list) -> None:
    # syötä tuote
    tuote = input("\nSyötä lisättävä tuote: ")

    # lisää tuote viitattuun listaan
    kauppalista.append(tuote)


# poista tuote funktio, määritetty parametri tyyppiä list
def poista_tuote(kauppalista: list) -> list:
    while True:
        # poistettava tuote
        print("\nKauppalistassa on: ", ", ".join(kauppalista)+"\n")
        poista = input("Syötä poistettava tuote: ").strip()

        if poista in kauppalista:
            kauppalista.pop(kauppalista.index(poista))
            break

        # jos input on jotain höperöä, hyppää ulos loopista
        break



def main():
    # funktion vakiomuuttuja
    kauppalista = []

    # ohjelman pää-loop
    while True:
        # valitse toiminto valikko_toiminto() funktiolla
        toiminto = valikko_toiminto()

        if int(toiminto) == 1:
            # Lisää tuote
            lisaa_tuote(kauppalista)
            
        elif int(toiminto) == 2:
            # Poista syötetty tuote
            poista_tuote(kauppalista)

        elif int(toiminto) == 3:
            # Tulosta kauppalista
            # jos listassa on tavaraa...
            if len(kauppalista) > 0:
                print("\nKauppalistassa on: ", ", ".join(kauppalista))
            else:
                print("\nKauppalistassa on: ", "\"Kauppalistasi on tyhjä.\"")

        elif int(toiminto) == 4:
            # tyhjennä kauppalista
            kauppalista.clear()
            print("\nKauppalista on nyt tyhjä!")

        else:
            # ohjelman lopetus
            print("\nKiitos ohjelman käytöstä.")
            break
    


if __name__ == "__main__":
    main()