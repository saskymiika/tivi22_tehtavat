

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
    strng = "this is my test string and I am going to use it now"

    for i in strng.split():
        match_object = re.match("[t-m]", i):

        if match_object:
            print(match_object.groups())

    # virke = input("Syötä jokin virke: ")
    # virkkeen_sanat = virke.split()
    # for sana in virkkeen_sanat:
        # if re.findall("", sana[0])



if __name__ == "__main__":
    main()