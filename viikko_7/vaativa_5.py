"""
Viikko 7 vaativa 5
Miika Toivanen
miika.toivanen@edu.sasky.fi

Tee funktio, joka selvittää, onko käyttäjän syöttämä sana palindromi.
"""

# vertaa merkkijonoa käännettyyn itseensä ja palauttaa boolean arvon.
def onko_palidromi(palindromi: str) -> bool:
    return palindromi[::-1] == palindromi


def main():
    palindromi = input("Syötä palindromi: ").strip()

    print(f"\nSyötit seuraavan palindromin: {palindromi}, joka on käänettynä: {palindromi[::-1]}.")

    if onko_palidromi(palindromi):
        print("Sana on palindromi!")
    else:
        print("Sana ei ole palindromi.")


if __name__ == "__main__":
    main()