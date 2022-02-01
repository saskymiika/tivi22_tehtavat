"""
Tehtävä 5.1
Miika Toivanen
miika.toivanen@edu.sasky.fi

Ohjelmoi lista, jossa on viisi katuosoitetta.

Tulosta lista niin, että kolmannen osoitteen perässä lukee “Ei pysäköintiä”.

Esimerkkiajo:

Oikopolku 2
Umpikuja 3
Tienhaara 5 - Ei pysäköintiä!
Välitie 6
Mikonkatu 4
Kiitos ohjelman käytöstä.

- Muista lisätä koodin kommentit jotka selittävät mitä ohjelma tekee.
"""


def main():
    # viisi katuosoitetta lista
    osoitteet = ["Oikopolku 2", "Umpikuja 3", "Tienhaara 5 - Ei pysäköintiä!", "Välitie 6", "Mikonkatu 4"]

    # looppaa läpi koko lista
    for osoite in osoitteet:
        print(osoite)

    print("Kiitos ohjelman käytöstä.")


if __name__ == "__main__":
    main()