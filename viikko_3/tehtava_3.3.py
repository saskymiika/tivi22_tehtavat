
# Tehtävä 3.3

# Tässä tehtävässä kerrataan laskuoperaattoreiden käyttöä.

# Tee ohjelma, joka pyytää käyttäjältä viisi arvosanaa yksi kerrallaan (välissä painetaan Enter-painiketta). Kun kaikki viisi arvosanaa on syötetty, ohjelma laskee syötettyjen viiden arvosanan keskiarvon ja ilmoittaa sen käyttäjälle. 

# Jos käyttäjä syöttää jotain kokonaisluvuksi kelpaamatonta, ohjelma opastaa käyttäjää. Ohjelman suoritus saa loppua tähän, mutta ohjelma ei saa kaatua. 

# Ohjelman esimerkkiajo:

# Syötä viisi arvosanaa, yksi kerrallaan.
# Syötä arvosana: 6
# Syötä arvosana: 7
# Syötä arvosana: 5
# Syötä arvosana: 4
# Syötä arvosana: 10
# Syötettyjen arvosanojen keskiarvo on: 6.4
# Kiitos ohjelman käytöstä.


def main():
    print("Syötä viisi arvosanaa, yksi kerrallaan.")

    # arvosanat lista, lisää tänne kaikki arvosanat
    arvosanat = []
    
    # monesko arvosana..?
    kerta = 1

    while True:
        # kysy arvosanaa
        arvosana = input("\nSyötä " +str(kerta) +". arvosana: ")

        # tarkista että syötetty arvo on kokonaisluku
        if arvosana.isdigit():
            # lisää arvosana arvosanat listaan, ja muuta tyyppi kokonaisluvuksi
            arvosanat.append( int(arvosana) )
            # lisää 1 kerta-muuttujaan
            kerta += 1

            # kun arvosanat listassa on 5 arvosanaa
            if len(arvosanat) >= 5:
                # break komennolla hyppää ulos while silmuksasta
                break

        else:
            print("\nOle hyvä ja käytä kokonaislukua!")


    # laskee arvosanojen keskiarvon
    keskiarvo = sum(arvosanat) / len(arvosanat)

    # tulosta keskiarvo
    print("\nSyötettyjen arvosanojen keskiarvo on:",'%.1f' % keskiarvo)
    print("\nKiitos ohjelman käytöstä!")


if __name__ == "__main__":
    main()