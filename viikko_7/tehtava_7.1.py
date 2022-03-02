"""
Tehtävä 7.1
Miika Toivanen
miika.toivanen@edu.sasky.fi


Kirjoita funktio joka ottaa argumenttina merkkijonon. Funktio muuttaa merkkijonon jokaisen sanan ensimmäisen kirjaimen kirjaimeksi "S" ja palauttaa muokatun merkkijonon pääohjelmalle.

Kutsu luomaasi funktiota ja anna sille argumenttina käyttäjän kirjoittama lause. Lopuksi tulosta funktion palauttama merkkijono ruudulle.
"""

# Muuttaa merkkijonon ensimmäisen kirjaimen 'S'-kirjaimeksi ja palauttaa uutena merkkijonona.
def oijoijoi(sana: str) -> str:
    return 'S' + sana[1:len(sana)]


def s_sanat(merkkijononi: str) -> str:
    # map() funcktiolla muotoillaan sille määritetty lista uuteen muotoon, apufunktioon määrätyllä menetelmällä
    # list() palauttaa map objektin oikeasti listana
    # " ".join() palauttaa listan merkkijonona sanat välilyönnillä erotettuina
    return " ".join(list(map(oijoijoi, merkkijononi.split())))


def main():
    print("\n -> "+s_sanat(input("Heitä jotain settiä: ")))


if __name__ == "__main__":
    main()
