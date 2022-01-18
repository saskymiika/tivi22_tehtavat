
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

def lisaa_arvosanat(lista, pituus):

    li = 0
    while li < pituus:
        arvosana = input("Syötä arvosana: ")

        #tarkista että syötetään numero
        if not arvosana.isdigit():
            print("Ole hyvä ja käytä kokonaislukua.")
            return

        # lisää arvosana listaan kokonaislukuna
        lista.append(int(arvosana))

        # increment loop index
        li += 1


def main():
    print("Syötä viisi arvosanaa, yksi kerrallaan.")

    # arvosanat lista, lisää tänne kaikki arvosanat
    arvosanat = []
    
    # itse tehty apufunktio, kysyy 5 kertaa arvosanaa ja lisää ne arvosanat-listaan
    lisaa_arvosanat(arvosanat, 5)

    # laskee arvosanojen keskiarvon
    keskiarvo = sum(arvosanat) / len(arvosanat)

    print("Syötettyjen arvosanojen keskiarvo on:",'%.1f' % keskiarvo)
    print("Kiitos ohjelman käytöstä!")


if __name__ == "__main__":
    main()