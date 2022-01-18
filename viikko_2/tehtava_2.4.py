# Tehtävä 2.4

# Jatka tehtävään 1.4 tekemääsi ohjelmaa.
# Kun käyttäjä vastaa kysymykseen "Kuinka vanha olet?" tarkista, että annettu vastaus oli numero. Jos kyseessä ei ollut numero tulosta ruudulle "Ole ystävällinen ja anna ikäsi numerona."
# Jos käyttäjä antoi numeron tulostus kuten tehtävässä 1.4.
# Muista noudattaa tyyliopasta.

# funtion joka kysyy kolmea lukua ja palauttaa ne yhteen arrayhin
from datetime import date

# käytä date modulia/kirjastoa
today = date.today()

# TEHTÄVÄ 1.4

# Tee ohjelma, joka kysyy käyttäjän nimeä ja ikää ja sen jälkeen 
# tulostaa: Ajattele "NIMI"! Vuonna 2042 olet jo (ikä + 20) vuotta vanha.

def main():
    # syötä nimi
    nimi = input("Syötä nimesi: ")

    # syötä ikä ja muuta data INT-muotoon
    # ika = int(input("Syötä ikäsi: "))
    ika = input("Syötä ikäsi: ")

    # tarkista että on luku on numeero
    if not(ika.isdigit()):
        print("Ole ystävällinen ja anna ikäsi numerona.")
        return

    # muuta ika kokonaisluvuksi
    ika = int(ika)
    
    # ero tästä vuodesta (2022) vuoteen 2042
    vuosia = 2042 - today.year

    # ikä vuoteen 2042 mennessä
    vuosia_ero = str(ika + vuosia)

    #näytä ika vuoteen 2042 mennessä
    print("Ajattele " + nimi + "! Vuonna 2042 olet jo "+ vuosia_ero +" vuotta vanha")


# kutsuu pääohjelman
if __name__ == "__main__":
    main()