# tehtävä 4.1

# Tee ohjelma joka kysyy käyttäjän nimeä. 
# Jos annetun nimen kolmas kirjain on s, ohjelma tulostaa Jee!. Jos jotain muuta ohjelma tulostaa Plääh!

# Esimerkki:

# Anna nimi: Kissa
# Jee!
# Anna nimi: Matti
# Plääh! 


def main():
    # kysy nimeä
    nimi = input("Mikä on nimesi? ")

    # tarkista että nimessä on vähintään 3 kirjainta!
    if len(nimi) < 3:
        print("Nimessäsi ei ole edes kolmea kirjainta!")
        return

    # tarkista käyttäjän nimen kolman kirjain
    if nimi[2] == 's':
        print("Jee!")
    else:
        print("Plääh!")


if __name__ == "__main__":
    main()