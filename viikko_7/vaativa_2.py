"""
Viikko 7 vaativa 2
Miika Toivanen
miika.toivanen@edu.sasky.fi


Koodaa ohjelma, joka kysyy ensin käyttäjältä syötteenä sanan ja sen jälkeen kuinka monta kertaa ko. sana tulostetaan näyttöön. Toteuta tulostustoiminto funktiona. Kun ohjelma kysyy tulostuskertoja se ilmoittaa käyttäjän syöttämän sanan, kuten seuraavasta esimerkkiajosta ilmenee:
"""


def tulosta_sanasi_niinjaniin_monta_kertaa(sana: str, kertaa: int) -> None:
    for x in range(kertaa):
        print(sana)


def main():
    sana = input("Syötä sana: ")

    while True:
        kertaa = input(f"Kuinka monta kertaa {sana} tulostetaan: ")

        if kertaa.isdigit():
            kertaa = int(kertaa)
            break
        else:
            print("Käytä kokonaislukua.")

    tulosta_sanasi_niinjaniin_monta_kertaa(sana, kertaa)


if __name__ == "__main__":
    main()