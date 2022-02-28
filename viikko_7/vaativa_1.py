"""
Viikko 7 vaativa 1
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

def funktiosta(virke: str) -> None:
    print(virke)

def sanasi(sana: str) -> None:
    print(f"Syötit sanan: {sana}")

def muodostuu(sanalista: list) -> None:
    # Syöttämistäsi sanoista kissa ja koira muodostuu yhdyssana: kissakoira.
    print(f"\nSyöttämistäsi sanoista {sanalista[0]} ja {sanalista[1]} muodostuu yhdyssana: {''.join(sanalista)}.")


def main():
    funktiosta("Tämä teksti tulostuu funktiosta.")

    sana1 = input("\nAnna sana: ")
    sanasi(sana1)

    sana2 = input("\nAnna toinen sana: ")
    sanasi(sana2)

    muodostuu([sana1, sana2])


if __name__ == "__main__":
    main()
