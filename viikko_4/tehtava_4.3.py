"""
Tehtävä 4.3
Miika Toivanen
miika.toivanen@edu.sasky.fi


Tulosta seuraavan merkkijonon pituus: "Hyvä koodi on kuin runo."

Tulosta saman merkkijonon 12 ensimmäistä merkkiä ensimmäiselle riville ja 12 viimeistä merkkiä toiselle riville. 
Edellisen esimerkkiajo:

Hyvä koodi o
n kuin runo.

Tulosta, mistä indeksistä alkaa sana "kuin".
- Muista lisätä koodin kommentit jotka selittävät mitä ohjelma tekee.

"""


def main():
    mjono = "Hyvä koodi on kuin runo."

    # tulosta merkkijonon pituus
    print(len(mjono))

    # valitse merkkijonosta 12 ensimmäistä merkkiä
    print(mjono[0:12])

    # tulosta loput merkkijonosta
    print(mjono[12:len(mjono)])

    # sanan kuin indeksi
    print("Sanan \"kuin\" indeksi:", mjono.find("kuin"))


if __name__ == "__main__":
    main()