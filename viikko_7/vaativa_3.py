"""
Viikko 7 vaativa 3
Miika Toivanen
miika.toivanen@edu.sasky.fi

Koodaa ohjelma, jossa käyttäjältä pyydetään kaksi lukuarvoa. Lisää funktio, joka testaa kumpi luvuista on suurempi. Funktion tulee tulostaa näytölle, kumpi luku on suurempi ja jos luvut ovat samat, tulee sen tulostaa näytölle teksti: “Syötetyt luvut luku1 ja luku2 ovat samansuuruiset”.
"""


def vertaa_arvoja(arvot: list) -> None:
    # sort() metodi järjestää listan tavarat pienimmästä suurimpaan...
    arvot.sort()

    # ...joten ensimmäinen on varmasti pienempi, joten jos luvut ovat erisuuruiset, niin tämä ehto on aina True.
    if arvot[1] > arvot[0]:
        print(f"Luku {arvot[1]} on suurempi kuin luku {arvot[0]}.")
    # Tai sitten.
    else:
        print(f"Syötetyt luvut {arvot[0]} ja {arvot[1]} ovat samansuuruiset.")


def main():
    while True:
        # strip() = tyhjät pois eestä ja takaa.
        # split() = erottaa merkkijonon syötteen " ":n perusteella ja palauttaa kaikki listana muuttujaan 
        kaksi_lukua = input("\nSyötä kaksi kokonaislukua välilyönnillä erotettuna: ").strip().split(" ")

        if len(kaksi_lukua) == 2:
            # tarkista että ovat kokonaislukuja
            if kaksi_lukua[0].isdigit() and kaksi_lukua[1].isdigit():
                # map() funktio muotoilee listan uudestaan, muutamalla arvot merkkijonosta kokonaisluvuksi
                # list() funktio ottaa map():n palauttaman arvon ja tekee siitä listan
                kaksi_lukua = list(map(lambda a : int(a), kaksi_lukua))
                # vertaa arvoja
                vertaa_arvoja(kaksi_lukua)
                break
            else:
                print("Lukusi eivät olleet kokonaislukuja. Koitappa uudelleen.")
        else:
            print("Siis KAKSI kokonaislukua.")


if __name__ == "__main__":
    main()