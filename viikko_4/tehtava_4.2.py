"""
Tehtävä 4.2
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

# Tee ohjelma, joka tulostaa joka kolmannen merkin seuraavasta merkkijonosta: "Ajattelen, siis olen!"

# Tulosta sama merkkijono käännettynä.
# Tulosta merkkijonosta sana: "olen"
# - Muista lisätä koodin kommentit jotka selittävät mitä ohjelma tekee.

def main():
    merkkijono = "Ajattelen, siis olen!"

    # merkkijono käännettynä
    print(merkkijono[::-1])

    # merkkijonosta sana "olen"
    # rsplit() tekee listan merkkijonon kaikista sanoista ja index [2] palauttaa listan viimeisen sanan
    # replace() metodi poistaa "!" ja korvaa sen tyhjällä "".
    print(merkkijono.rsplit()[2].replace("!", ""))


if __name__ == "__main__":
    main()