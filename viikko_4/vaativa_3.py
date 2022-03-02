"""
Viikko 4 vaativa tehtävä 3
Miika Toivanen
miika.toivanen@edu.sasky.fi

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
    while True:
        valintanumero = input("\nValitse seuraavista:\n1 = Syötä virke\n2 = Kirjainalue, jolta sanat tulostetaan\n3 = Tulosta sanat\n0 = Lopeta\n\nValintasi: ").strip()

        # jos annettu arvo on kokonaisluku ja on jokin annetuista vaihtoehdoista,
        # funktio palauttaa annetun arvon
        if valintanumero.isdigit():
            valintanumero =  int(valintanumero)
            if valintanumero < 4:
                return valintanumero
            else:
                print('Koitappa lukuja 1, 2, 3 tai 0.\n')

        else:
            print('Et ny oikeen osaa. Koitappa lukuja 1, 2, 3 tai 0.\n')
        

def main():
    # ohjelman vakiomuuttujia
    virke = ""
    ka_1, ka_2 = None, None

    while True:
        # valitse toiminto ohjelmalle
        toiminto = valinta()

        if toiminto == 1:
            # syötä virke
            virke = input("\nSyötä jokin virke: ").strip()

        elif toiminto == 2:
            # valitse kirjainalue
            # [0] indeksillä varmistan ettei mukaan tule enemmän kuin yksi kirjain.
            ka_1 = input("\nMillä kirjain välillä halutaan sanat tulostaa, alku: ")[0]
            ka_2 = input("Millä kirjain välillä halutaan sanat tulostaa, loppu: ")[0]

        elif toiminto == 3:
            # tulosta sanat
            # tarkista että virke on annettu
            if len(virke) > 0:
                # tarksita että kirjainalue on määritetty
                if ka_1 == None or ka_2 == None:
                    print("\nMääritä kirjainalue!")
                else:
                    # kaikki sanat regular expressionin mukaan
                    sanat = re.findall(r"\b[%s-%s]\w+" % (ka_1, ka_2), virke) 
                    print("\nVirkkeessä oli kirjaimilla %s-%s alkavia sanoja seuraavat:" % (ka_1, ka_2))

                    for v in sanat:
                        print(v.upper())

            else:
                print("\nEt ole vielä syöttänyt virkettä!")

        elif toiminto == 0:
            print("\nKiitos ohjelman käytöstä!")
            break
    

if __name__ == "__main__":
    main()
