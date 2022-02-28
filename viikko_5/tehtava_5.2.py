"""
Tehtävä 5.2
Miika Toivanen
miika.toivanen@edu.sasky.fi


Tee seuraava ohjelma while-silmukalla hyödyntäen .append()-metodia.
Ohjelma kysyy käyttäjältä syntymäpäivää ja lisää sen listaan. Seuraavaksi ohjelma kysyy uutta syntymäpäivää ja lisää sen listaan. Ohjelma kysyy syntymäpäivä, kunnes käyttäjä syöttää l-kirjaimen = lopeta. Lopussa ohjelma tulostaa syntymäpäivälistan.

Esimerkkiajo:

Syötä syntymäpäivä: 11.12.2001
Syötä syntymäpäivä: 1.3.2003
Syötä syntymäpäivä: 20.5.1999
Syötä syntymäpäivä: l

Syötit seuraavat syntymäpäivät:

11.12.2001
1.3.2003
20.5.1999

Kiitos ohjelman käytöstä.

- Muista lisätä koodin kommentit jotka selittävät mitä ohjelma tekee.
"""

from calendar import month
import re
from datetime import datetime

def main():
    # syntymäpäivälista
    syntymapaivat = []
    tama_paiva = datetime.now()

    # laske kuinka mones vuosi on vuodesta 1900
    taydet_vuodet = tama_paiva.year - 1900 -1
    taydet_paivat = (taydet_vuodet * 365.25) + tama_paiva.day

    def tamanvuoden_paivat(kk, pp, vsi):
        pvt = pp
        kkdn_paivat = [31,28,31,30,31,30,31,31,30,31,30,31]
        # lisää kaikki päivät kaikista tämän vuoden kuukausista taydet_paivat muuttujaan
        for m in range(kk):
            # jos olemme tämänhetkisessä kuukaudessa, poistu silmukasta
            if m+1 == kk: 
                break
            pvt += kkdn_paivat[m]

            # jos on helmikuu ja tämä vuosi on karkausvuosi
            if m == 1:
                if vsi % 4 == 0:
                    pvt += 1
        
        return pvt

    taydet_paivat += tamanvuoden_paivat(tama_paiva.month, tama_paiva.day, tama_paiva.year)

    print('Syötä syntymäpäiviä muodossa pp.kk.vvvv\n')

    # while-silmukka, kysyy sp:ä kunnes arvoksi annetaan "l"
    while True:
        sp = input("Syötä syntymäpäivä: ")

        # jos arvo on "l", hyppää ulos while silmukasta
        if sp == "l":
            break

        reg_obj = re.search(r'\b\d{2}\.\d{2}\.\d{4}\b', sp)

        if reg_obj != None:
            syntpvm = sp[reg_obj.start():reg_obj.end()]
            pp = syntpvm.split('.')[0]
            kk = syntpvm.split('.')[1]
            vvvv = syntpvm.split('.')[2]
            if int(pp) <= 31:
                if int(kk) <= 12:
                    if int(vvvv) <= tama_paiva.year:
                        tv = int(vvvv) - 1900 -1
                        tp = (tv * 365.25) + int(pp)
                        tp += tamanvuoden_paivat(int(kk), int(pp), int(vvvv))
                        if tp <= taydet_paivat:
                            syntymapaivat.append(syntpvm)
                        else: 
                            print('Syöttämäsi päivämäärä ei voi olla suurempi kuin tämä päivä.')
                else:
                    print('Ei voi olla suurempi kuukausi kuin 12. Sinä syötit', kk)
            else:
                print('Ei voi olla kuukaudessa enempää päiviä kuin 31. Sinä syötit', pp)
        else:
            print('Käytä syntymäpäivässä muotoa pp.kk.vvvv\n')
    

    print("\nSyötit seuraavat syntymäpäivät:\n")

    # tulosta syntymäpäivälistan
    for sp in syntymapaivat:
        print(sp)

    print("\nKiitos ohjelman käytöstä.")


if __name__ == "__main__":
    main()