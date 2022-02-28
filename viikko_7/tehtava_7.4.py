"""
Tehtävä 7.4
Miika Toivanen
miika.toivanen@edu.sasky.fi


## Kirjoita funktio, joka ottaa argumenttina merkkijonon ja printtaa sen ruudulle. Jos funktiota kutsuttaessa parametria ei anneta, tulosta ruudulle "Ei sanottavaa". Eli funktiolla on oletusparametri, joka on "Ei sanottavaa."

Älä kysy käyttäjältä lausetta, vaan määritä se itse pääohjelmassa. Kirjoita pääohjelmaan useampi funktion kutsu, joista osassa on argumentti ja osassa ei ole argumenttia.

Kirjoita ohjelma joka käyttää tätä funktiota.
"""

# funktio jossa lause parametrin arvo määritetty valmiiksi = "Ei sanottavaa"
def tulosta_lause(lause="Ei sanottavaa."):
    print(lause)


def main():
    # Palauttaa lauseet listaan.
    lauseet = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Fusce posuere varius venenatis.
Donec lacinia nisl et magna ultrices, sit amet rutrum ante sollicitudin.
Aliquam tempus faucibus est, sed pretium lacus bibendum ut.
Nam aliquet ac augue ac dignissim.
Quisque rhoncus ligula et ligula aliquam accumsan.
Nunc elementum suscipit mi et cursus.
Nulla facilisi.
Sed faucibus hendrerit quam sed consectetur.""".split("\n")
    
    # Tulostaa jokaisen lauseen listasta, mikä ei ole määrätyssä indekseissä.
    i = 0
    while i < len(lauseet):
        if i == 1 or i == 3 or i == 6:
            tulosta_lause()
        else:
            tulosta_lause(lauseet[i])

        i += 1


if __name__ == "__main__":
    main()
    