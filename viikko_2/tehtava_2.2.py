"""
Tehtävä 2.2
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

# Tee ohjelma, joka pyytää käyttäjän suosikkieläintä. Jos käyttäjän suosikkieläin on kissa, tulostetaan: "Taidat olla kissaihmisiä." Jos käyttäjä antaa minkä tahansa muun eläimen, tulostetaan: "Ei ole kissaa karvoihin katsominen,"

# Tee ohjelmasi siten, että kissa == Kissa == KISSA, eli ohjelma hyväksyy sanan samaksi riippumatta isoista ja pienistä kirjaimista.

# Vinkki: Googleta merkkijonon metodeita (python string methods). 


def main():
    # syötä arvo muuttujalle
    onko_se_kissa = input("Ole hyvä ja syötä suosikki eläimesi: ")

    # casefold() metodi muuttaa kaikki kirjaimet pieniksi ja vertaa sen jälkeen
    # voisi käyttää myös string.lower() tai string.upper() metodia
    if onko_se_kissa.casefold() == "kissa":
        print("Taidat olla kissaihmisiä")
    else:
        print("Ei ole kissaa karvoihin katsominen")


if __name__ == "__main__":
    main()