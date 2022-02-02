"""
Viikko 3 vaativa tehtävä 3
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

# Laajenna vielä edellistä ohjelmaa siten, että se kysyy ensin käyttäjältä lukualueen, jolle arvattava numero halutaan sijoittaa. Sen jälkeen ohjelma näyttää alueen ja pyytää valitsemaan luvun alueelta. Viimeiseksi ohjelma pyytää käyttäjää arvaamaan oikean luvun. Käyttäjällä on viisi arvauskertaa käytössään.

from random import randint 


def main():
    print("Arvaa oikea luku!")
    
    lukualue = []

    while True:
        # syötä merkkijono ja ottaa pois kaikki välilyönnit
        arvo = input("\nSyötä lukualue, jonka perusteella arvattava luku valitaan.\nSyötä lukualue muodossa 10-20.\n\nLukualueesi: ").strip().replace(" ", "")
        
        # jos syötetystä arvosta löytyy merkki "-"
        if arvo.find("-") != -1: 
            # erota - merkin perusteella arvot listaan
            arvo = arvo.split("-")
            
            # jos on syötetty vähemmän tai enemmän kuin kaksi arvoa
            if len(arvo) != 2:
                print('ole hyvä ja syötä KAKSI kokonaislukua')

            # jos kaksi...
            else:
                for a in arvo:
                    # jos luku ei ole kokonaisluku
                    if not a.isdigit():
                        print('käytä kokonaislukuja...')
                        # tyhjennä lista vanhoista
                        lukualue.clear()
                        break
                    # jos on kokonaisluku lisää sen listaan INT-muodossa
                    else:
                        lukualue.append(int(a))
        # jos ei ole käytetty "-" merkkiä
        else:
            print('VIRHE! Erota luvut toisistaa merkillä "-"')

        # kun meillä on vihdoinkin ne kaksi kokonaislukua.. hyppää ulos silmukasta
        if len(lukualue) >= 2:
            break

    # sort() metodi järjestää listan uudelleen pienimmästä suurimpaan
    lukualue.sort()

    print(f'\nArvattava luku valitaan {lukualue[0]} ja {lukualue[1]} väliltä')
    
    # valitse luku satunnaisesti syötetun lukuarvon väliltä
    luku = randint(lukualue[0], lukualue[1])

    # yrityksiä muuttuja
    yrityksia = 5

    while True:
        # jos yrityksiä on alle 1, lopeta ohjelma
        if yrityksia < 1:
            print("\nEt arvannut oikeaa lukua. Oikea luku oli:", luku)
            break

        # tulosta yrityksiä jäljellä
        print("\nSinulla on "+str(yrityksia)+" yritystä jäljellä")

        # kysy lukua
        arvaus = input(f"\nSyötä luku {lukualue[0]}-{lukualue[1]} väliltä.\n\nLukusi: ")

        # tarkista että syötetty arvo on kokonaisluku
        if arvaus.isdigit():
            # vertaa arvausta annettuu lukuu
            if int(arvaus) < luku:
                print("Lukusi on liian PIENI.")
            elif int(arvaus) > luku:
                print("Lukusi on liian SUURI.")
            else:
                print("\nHienoa! Arvasit oikein!")
                print("\nKiitos ohjelman käytöstä.")
                break

            # vähennä yrityksiä
            yrityksia -= 1
        else:
            print("\nOle hyvä ja käytä kokonaislukua.")


if __name__ == "__main__":
    main()