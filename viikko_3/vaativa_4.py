"""
Viikko 3 vaativa tehtävä 4
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

# Laajenna vielä edellistä ohjelmaa siten, että se kysyy, montako arvauskertaa käyttäjälle annetaan. Jos käyttäjä arvaa oikean luvun kertojen sisällä, onnittele häntä, ja ilmoita, montako arvausta jäi käyttämättä. Tällä kertaa ohjelma näyttää arvausten alussa niiden jäljellä olevan määrän.

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
                print('Ole hyvä ja syötä KAKSI kokonaislukua')

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

    # valitse luku satunnaisesti lukualueen väliltä
    luku = randint(lukualue[0], lukualue[1])

    # yrityksiä muuttuja
    arvauksia = ""
    visual_arvauksia = []

    # tulostaa arvausten määrät
    def print_visual_list(list):
        index = len(list) - arvauksia
        for x in range(index):
            if list[x] != "#":
                list[x] = "#"
        print("\n["+("|".join(list))+"]")


    # kysy arvausten määrää
    while True:
        arvauksia = input("\nKuinka monta arvauskertaa sallitaan? ")
        if arvauksia.isdigit():
            # muuta arvauksia muutuja kokonaisluvuksi ja hyppää ulos...
            arvauksia = int(arvauksia)
            # lisää visaul listaan arvauskerrat
            for x in range(arvauksia):
                visual_arvauksia.append('_')
            break
        else:
            print('Syötä kokonaisluku!')


    while True:
        # jos yrityksiä on alle 1, lopeta ohjelma
        if arvauksia < 1:
            print("\nEt arvannut oikeaa lukua. Oikea luku oli:", luku)
            break

        # tulosta yrityksiä jäljellä
        print_visual_list(visual_arvauksia)
        print("Sinulla on "+str(arvauksia)+"/"+str(len(visual_arvauksia))+" yritystä jäljellä")

        # kysy lukua
        arvaus = input("\nSyötä luku "+str(lukualue[0])+" - "+str(lukualue[1])+" väliltä.\nLukusi: ")

        # tarkista että syötetty arvo on kokonaisluku
        if arvaus.isdigit():
            # vertaa arvausta annettuu lukuu
            if int(arvaus) < luku:
                print("Lukusi on liian PIENI.")
            elif int(arvaus) > luku:
                print("Lukusi on liian SUURI.")
            else:
                print("\nHienoa! Arvasit oikein!", "Arvauksia jäi jäljelle:", arvauksia)
                print("\nKiitos ohjelman käytöstä.")
                break

            # vähennä yrityksiä
            arvauksia -= 1
        else:
            print("\nOle hyvä ja käytä kokonaislukua.")


if __name__ == "__main__":
    main()