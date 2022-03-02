"""
Viikko 4 vaativa tehtävä 2
Miika Toivanen
miika.toivanen@edu.sasky.fi

Lisää edelliseen ohjelman toiminnallisuus, jossa se pyytää syöttämään virkkeen ja kysyy seuraavaksi, millä kirjainvälillä sanat halutaan tulostaa.

Esimerkkiajo:

Syötä virke: Mustan kissan paksut posket, jyrkän penkereen reunalla.
Millä kirjain välillä halutaan sanat tulostaa, alku: a
Millä kirjain välillä halutaan sanat tulostaa, loppu: l

Virkkeessä oli kirjaimilla a-l alkavia sanoja seuraavat:
KISSAN
JYRKÄN

Kiitos ohjelman käytöstä.
"""

import re

def main():
    virke = input("Syötä jokin virke: ")
    alku  = input("Millä kirjain välillä halutaan sanat tulostaa, alku: ").strip()
    loppu = input("Millä kirjain välillä halutaan sanat tulostaa, loppu: ").strip()

    # etsi sanat virkkeestä regular expressionin avulla
    # re.findall() metodi palauttaa kaikki sille määritetyt virkkeet listan muodossa
    sanat = re.findall(r"\b[%s-%s]\w+" % (alku, loppu), virke) 

    # muuttujien "placeholderi" voidaan lisätä merkkijonoon %s-merinnällä
    # muuttuja määritetään merkkijonon perään %-virkkeellä (1_muuttuja, 2_muuttuja)
    print("\nVirkkeessä oli kirjaimilla %s-%s alkavia sanoja seuraavat:\n" % (alku, loppu))

    for v in sanat:
        print(v.upper())
    
    print("\nKiitos ohjelman käytöstä!")


if __name__ == "__main__":
    main()

