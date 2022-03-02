"""
Viikko 8 vaativat tehtävät
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

import random

def main():
    while True:
        # Pyydä syötettä. Tallenna listana split() metodilla.
        runo = input('Syötä vähintään viisi sanaa sisältävä runo tai sanonta: ').strip().split()

        # Tarkista runo-listan pituus. Jos sanoja on 5 tai enemmän, hyppää ulos silmukasta.
        if len(runo) >= 5:
            break
    
    
    # Sekoita sanat listoissa tällä funktiolla. 
    def sana_sekoitin(l: list):
        # Järjestä lista nousevaan järjestyskeen.
        l.sort()

        pienet_kirjaimet = []
        isot_kirjaimet = []

        # Tarkista runo-listan sanat
        for sana in l:
            # Jos sanan pituus 3 tai alle, lisää "pienet_kirjaimet" listaan.
            if len(sana) <= 3:
                pienet_kirjaimet.append(sana.lower())
            
            # Jos sanan pituus on 7 tai enemmän, lisää "isot_kirjaimet" listaan.
            elif len(sana) >= 7:
                isot_kirjaimet.append(sana.upper())


        # Yhdistä listat yhdeksi uudeksi listaksi
        # overraidaa listoissa toistuvat sanat keskenään.
        for sana in l:
            for s in pienet_kirjaimet:
                if s.lower() == sana.lower():
                    l[l.index(sana)] = s.lower()
        
        # uuestaan sama.
        for sana in l:
            for s in isot_kirjaimet:
                if s.upper() == sana.upper():
                    l[l.index(sana)] = s.upper()
        
        # Sekoita listan järjestys
        random.shuffle(l)

        # uusi lista merkkijonona
        return l
            
    # Tulosta funktion arvo merkkijonoksi muutettuna.
    print("\nRuno tai sanonta järjestettynä uudelleen:", " ".join(sana_sekoitin(runo)))
    print("\nKiitos ohjelman käytöstä.")


if __name__ == "__main__":
    main()