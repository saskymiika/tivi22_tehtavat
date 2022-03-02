"""
Tehtävä 2.4
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

# Jatka tehtävään 1.4 tekemääsi ohjelmaa.
# Kun käyttäjä vastaa kysymykseen "Kuinka vanha olet?" tarkista, että annettu vastaus oli numero. Jos kyseessä ei ollut numero tulosta ruudulle "Ole ystävällinen ja anna ikäsi numerona."
# Jos käyttäjä antoi numeron tulostus kuten tehtävässä 1.4.
# Muista noudattaa tyyliopasta.

from datetime import date


def main():
    # syötä nimi
    nimi = input("Syötä nimesi: ").strip().title()

    # syötä ikä
    ika = input("Syötä ikäsi: ")

    # tarkista että on luku on numeero
    if not(ika.isdigit()):
        print("Ole ystävällinen ja anna ikäsi numerona.")
        return

    # muuta ika kokonaisluvuksi
    ika = int(ika)

    # thae tämänpäivän tiedot date.today() metodilla 
    today = date.today()
    
    # ero tästä vuodesta (2022) vuoteen 2042
    vuosia = 2042 - today.year

    # ikä vuoteen 2042 mennessä
    vuosia_ero = str(ika + vuosia)

    #näytä ika vuoteen 2042 mennessä
    print("Ajattele " + nimi + "! Vuonna 2042 olet jo "+ vuosia_ero +" vuotta vanha")


# kutsuu pääohjelman
if __name__ == "__main__":
    main()