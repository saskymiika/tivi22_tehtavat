"""
Viikon 10 Projektitehtävä
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

import io, os


def main():
    aa_dir = os.path.dirname(__file__)+'\\alkuaineet.txt'
    alkuaineet = []
    arvatut = []

    # tuo alkuaineet tiedostosta listaan
    with io.open(aa_dir, 'r', encoding='utf-8') as f:
        alkuaineet = f.read().strip().split('\n')
        f.close()

    # muotoile alkuaineet listaa uudelleen
    for a in alkuaineet:
        alkuaineet[alkuaineet.index(a)] = a.split(', ')

    print('Kerro viisi ensimmäisistä 20:stä alkuaineesta jaksollisessa järjestelmässä.')

    arvaus = 1

    # Ohjelman pääsilmukka, joka kysyy alkuaineita ja lisää ne arvatut listaan.
    while True:
        # Kysy alkuainetta
        aine = input('\nAine '+str(arvaus)+': ').strip()

        sama = False
        # Tarkista ettei ole sama kuin edellinen
        for a in arvatut:
            if a['arvaus'].lower() == aine.lower():
                print(f'{aine} oli jo syötetty. Duplikaatit eivät ole sallittuja.')
                sama = True
                break

        if sama:
            continue
        
        arvaus += 1
        # luo arvaus dictionary
        arvaus_dict = {'arvaus': aine, 'jarjestysluku': None}

        # Tarkista osuvuus alkuaineista
        for a in alkuaineet:
            # Jos arvaus on yhtä paljon kuin alkuaineen lyhenne tai nimike, lisää yksi piste
            if aine.lower() == a[0].lower() or aine.lower() == a[1].lower():
                arvaus_dict['jarjestysluku'] = a[2]
                break

        # Lisää arvatut listaan
        arvatut.append(arvaus_dict)

        # Kun arvauksia on 5, hyppää ulos silmukasta
        if len(arvatut) >= 5:
            break

    # Kun arvaukset on tehty

    # pisteet
    pisteet = 0

    taitotaso = ['SURKEA','Heikko','Tiedät vähän','Keskiverto', 'Hyvä', 'LEGENDA']
    
    for arvaus in arvatut:
        tulos = 'Väärin'

        if arvaus['jarjestysluku'] != None:
            if int(arvaus['jarjestysluku']) <= 20:
                pisteet += 1
                tulos = 'Oikein'

        arvatut[arvatut.index(arvaus)] = tulos + ': ' + arvaus['arvaus'].title()


    print('\n'+str(int((pisteet/5) * 100))+' % oikein.', ', '.join(arvatut))

    print('\nTaitotaso: '+taitotaso[pisteet])

    print('\nKiitos ohjelman käytöstä.')
    


if __name__ == "__main__":
    main()