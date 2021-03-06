# 1. Tehtävä:

# Tee ohjelma, joka kysyy käyttäjän nimeä ja ikää ja sen jälkeen 
# tulostaa: Ajattele "NIMI"! Vuonna 2042 olet jo (ikä + 20) vuotta vanha.

# Vinkki: Iän muuttujatyyppi pitää vaihtaa, jotta sillä voi suorittaa yhteenlaskua.
# Nimi siis kokonaan isoilla kirjaimilla.

from datetime import date



def main():
    # syötä nimi, strip() poistaa tyhjät, title() muuttaa otsikko muotoon
    nimi = input("Syötä nimesi: ").strip().title()

    # syötä ikä ja muuta data INT-muotoon
    ika = int(input("Syötä ikäsi: "))

    # käytä datetime modulia/kirjastoa
    today = date.today()
    
    # ero tästä vuodesta (2022) vuoteen 2042
    vuosia = 2042 - today.year

    # ikä vuoteen 2042 mennessä
    vuosia_ero = str( ika+vuosia )

    #näytä ika vuoteen 2042 mennessä
    print("Ajattele " + nimi + "! Vuonna 2042 olet jo "+ vuosia_ero + " vuotta vanha")


# kutsuu pääohjelman
if __name__ == "__main__":
    main()