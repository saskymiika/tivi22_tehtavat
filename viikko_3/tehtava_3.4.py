"""
Tehtävä 3.4
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

# Lisää edelliseen ohjelmaan toiminto, jossa ohjelma kysyy, montako arvosanaa käyttäjä aikoo syöttää. Lopuksi ohjelma laskee syötettyjen arvosanojen keskiarvon. Toteuta silmukka while-rakenteella.


def main():
    # arvosanat lista, lisää tänne kaikki arvosanat
    arvosanat = []

    arvosanojen_maara = 0

    # kysyy koinka monta arvosanaa ohjelma tulee pyytämään
    while True:
        maara = input("Määritä kuinka monta arvosanaa kysytään.\n\nSyötä kokonaisluku: ")

        if maara.isdigit():
            arvosanojen_maara = int(maara)
            break
        else:
            print("\nKÄYTÄ KOKONAISLUKUA.")

    
    # monesko arvosana..? pidän tällä kirjaa siitä monettako arvosanaa kysytään.
    mones = 1

    while True:
        # kysy arvosanaa
        arvosana = input("\nSyötä " +str(mones) +". arvosana: ")

        # tarkista että syötetty arvo on kokonaisluku
        if arvosana.isdigit():
            # lisää arvosana arvosanat listaan, ja muuta tyyppi kokonaisluvuksi
            arvosanat.append( int(arvosana) )
            # lisää 1 kerta-muuttujaan
            mones += 1

            # kun arvosanat listassa on arvosanojen_maara arvosanaa
            if len(arvosanat) >= arvosanojen_maara:
                # break komennolla hyppää ulos while silmuksasta
                break

        else:
            print("\nOle hyvä ja käytä kokonaislukua!")


    # laskee arvosanojen keskiarvon
    keskiarvo = sum(arvosanat) / len(arvosanat)

    # tulosta keskiarvo
    print("\nArvosanat:", arvosanat, "\n", "\nSyötettyjen arvosanojen keskiarvo on:",'%.1f' % keskiarvo)
    print("\nKiitos ohjelman käytöstä!")


if __name__ == "__main__":
    main()