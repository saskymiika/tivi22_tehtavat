"""
3. Tehtävä

Lisää edelliseen ohjelmaan valikkorakenne, jossa 0 (nolla) lopettaa ohjelman suorituksen.

Esimerkkiajo:

Ajo1:
Valitse seuraavasta:
1 = Syötä virke
2 = Kirjainalue, jolta sanat tulostetaan
3 = Tulosta sanat
0 = Lopeta
Valintasi: 1

Syötä virke: Mustan kissan paksut posket, jyrkän penkereen reunalla.

Valitse seuraavasta:
1 = Syötä virke
2 = Kirjainalue, jolta sanat tulostetaan
3 = Tulosta sanat
0 = Lopeta
Valintasi: 2

Anna kirjainalue, jolta väliltä virkkeen sanat tulostetaan: a-e

Valitse seuraavasta:
1 = Syötä virke
2 = Kirjainalue, jolta sanat tulostetaan
3 = Tulosta sanat
0 = Lopeta
Valintasi: 3

Virkkeessä oli kirjaimilla a-e alkavia sanoja seuraavat:
Ei yhtään sanaa halutulla kirjainvälillä!
"""

import re

def valinta():
    kertoja = 0

    while True:
        valintanumero = input("\nValitse seuraavista:\n1 = Syötä virke,\n2 = Kirjainalue, jolta sanat tulostetaan\n3 = Tulosta sanat\n0 = Lopeta\n\nValintasi: ")

        # jos annettu arvo on kokonaisluku ja on jokin annetuista vaihtoehdoista,
        # funktio palauttaa annetun arvon
        if valintanumero.isdigit() and len(valintanumero) == 1:
            return valintanumero
        else:
            if kertoja == 1:
                print('Et ny oikeen osaa. Koitappa lukuja 1, 2, 3 tai 0.\n')
            elif kertoja > 1:
                print('KESKITY! Syötä 1, 2, 3 tai 0\n')
            else:
                print('Ole hyvä ja yritä uudelleen.\n')

            kertoja += 1
        


def main():

    # ohjelman vakiomuuttujia
    virke = ""
    ka_1 = None
    ka_2 = None

    while True:
        # valitse toiminto ohjelmalle
        toiminto = int(valinta())

        if toiminto == 1:
            # syötä virke
            virke = input("\nSyötä jokin virke: ")

        elif toiminto == 2:
            # valitse kirjainalue
            ka_1  = input("\nMillä kirjain välillä halutaan sanat tulostaa, alku: ")
            ka_2 = input("Millä kirjain välillä halutaan sanat tulostaa, loppu: ")

        elif toiminto == 3:
            # tulosta sanat
            # tarkista että virke on annettu
            if len(virke) > 0:
                # tarksita että kirjainalue on määritetty
                if not(ka_1 == None) and not(ka_2 == None):
                    # kaikki sanat regular expressionin mukaan
                    sanat = re.findall(r"\b[%s-%s]\w+" % (ka_1, ka_2), virke) 
                    print("\nVirkkeessä oli kirjaimilla %s-%s alkavia sanoja seuraavat:" % (ka_1, ka_2))

                    for v in sanat:
                        print(v.upper())

                else:
                    print("\nEt ole vielä määrittänyt kirjainaluetta!")

            else:
                print("\nEt ole vielä syöttänyt virkettä!")

        elif toiminto == 0:
            print("\nKiitos ohjelman käytöstä!")
            break
    


if __name__ == "__main__":
    main()

