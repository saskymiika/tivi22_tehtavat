

"""
Tehtävä 1

Tee ohjelma, joka pyytää syöttämään virkkeen. Virkkeen syötön jälkeen, ohjelma tulostaa isoilla kirjaimilla kaikki ne sanat, jotka alkavat kirjaimilla l-ö.

Esimerkkiajo:

Syötä virke: Mustan kissan paksut posket, jyrkän penkereen reunalla.

Virkkeessä oli kirjaimilla l-ö alkavia sanoja seuraavat:
MUSTA
PAKSUT
POSKET
PENKEREEN
REUNALLA

Kiitos ohjelman käytöstä.
"""

import re

def main():
    virke = input("Syötä jokin virke: ")

    # etsi sanat virkkeestä regular expressionin avulla
    #re.findall() metodi palauttaa kaikki sille määritetyt virkkeet listan muodossa
    sanat = re.findall(r"\b[l-ö]\w+", virke) 
    
    print("\nVirkkeessä oli kirjaimilla l-ö alkavia sanoja seuraavat:\n")

    for v in sanat:
        print(v.upper())
    
    print("\nKiitos ohjelman käytöstä!")


if __name__ == "__main__":
    main()

