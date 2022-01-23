"""
Tehtävä 5.3

Korjaa ohjelmat toimiviksi:

Ohjelma01:

hinnat = [3, 5, 4, 2]
print("Tuotteiden 3 ja 4 yhteen laskettu hinta on:", hinnat[3] + hinnat[4])

Ohjelma02:

kolme_numeroa = [1, 1, 2]
print("Listan viimeinen alkio on: ", kolme_numeroa[3])

Ohjelma03:


puulista = "Mänty"
print("Puulista aiemmin: ", puulista)
puulista.insert(1,"Koivu")
print("Puulista lisäyksen jälkeen: ", puulista)
"""

def main():
    # Ohjelma01:n korjaus
    # indeksit ovat tulostuskomennossa pielessä.
    # tuote 3 on hinnat[2], ja tuote 4 on hinnat[3]

    hinnat = [3, 5, 4, 2]
    print("Tuotteiden 3 ja 4 yhteen laskettu hinta on:", hinnat[2] + hinnat[3])

    # Ohjelma02:n korjaus
    # listan viimeinen indeksi on [2]

    kolme_numeroa = [1, 1, 2]
    print("Listan viimeinen alkio on: ", kolme_numeroa[2])

    # Ohjelma03:n korjaus
    # muuta puulista-muuttuja merkkijonosta listaksi

    puulista = ["Mänty"]
    print("Puulista aiemmin: ", puulista)

    # listan insert() metodi lisää arvon määritettyyn indexiin
    puulista.insert(3,"Koivu")
    print("Puulista lisäyksen jälkeen: ", puulista)


if __name__ == "__main__":
    main()