"""
Viikko 7 vaativa 4
Miika Toivanen
miika.toivanen@edu.sasky.fi

Huomaa pisteeseen loppuvat rivit eli pisteen tulee olla virkkeen viimeisessä sanassa tai muuttujan arvossa kiinni. Huomaa myös, että ohjelman tulosteiden välissä on rivinvaihto.
"""


def palindroma(merkkijononi: str) -> str:
    return merkkijononi[::-1]
    

def main():
    teksti = input("Syötä teksti: ").strip()

    # Varmaan haluamme käyttää funktiota tähän kun olemme viikossa 7 ???
    print(f"\nSyöttämäsi teksti on palindromina: {palindroma(teksti)}")


if __name__ == "__main__":
    main()