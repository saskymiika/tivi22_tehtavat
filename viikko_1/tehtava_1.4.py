from datetime import date

# käytä date modulia/kirjastoa
today = date.today()

# TEHTÄVÄ 1.4

# Tee ohjelma, joka kysyy käyttäjän nimeä ja ikää ja sen jälkeen 
# tulostaa: Ajattele "NIMI"! Vuonna 2042 olet jo (ikä + 20) vuotta vanha.

# Vinkki: Iän muuttujatyyppi pitää vaihtaa, jotta sillä voi suorittaa yhteenlaskua.
# Nimi siis kokonaan isoilla kirjaimilla.


def main():
    # syötä nimi
    nimi = input("Syötä nimesi: ")

    # syötä ikä ja muuta data INT-muotoon
    ika = int(input("Syötä ikäsi: "))
    
    # ero tästä vuodesta (2022) vuoteen 2042
    vuosia = 2042 - today.year

    # ikä vuoteen 2042 mennessä
    vuosia_ero = str( ika+vuosia )

    #näytä ika vuoteen 2042 mennessä
    print("Ajattele " + nimi + "! Vuonna 2042 olet jo "+ vuosia_ero + " vuotta vanha")


# kutsuu pääohjelman
if __name__ == "__main__":
    main()