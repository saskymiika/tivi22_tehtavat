"""
Viikko 11 vaativat
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

import os
from random import randint


def main():
    # Ja näin tähän alkuun olen päättänyt että tehtävässä käytettävä hakemisto 
    # on tämän viikko_11 sisällä oleva alihakemisto nimeltä subdirs.

    def onko_hakemisto_olemassa(dir_path: str, dir_name: str):
        # tarkista onko kansio jo olemassa
        dir_on_olemassa = False
        for dir in os.scandir(dir_path):
            if dir.is_dir() and dir.name == dir_name:
                dir_on_olemassa = True
                break
        return dir_on_olemassa

    def kansio_kpl_maara():
        # Pituus of
        #   thelist of
        #       file names of
        #           diractorypath
        #               if instance is directory
        #                   adds to the list
        # ===> len(thelist)
        return len([f.name for f in os.scandir(os.path.dirname(__file__) + '\\subdirs') if f.is_dir()])

    def nimi_genraattori():
        # random ints. lisää ylimääräsen nollan jos ei ole tarpeeksi pituutta zfill() metodilla
        pp = str(randint(1, 31)).zfill(2)
        kk = str(randint(1, 12)).zfill(2)
        vv = str(randint(1, 99)).zfill(2)
        rint = str(randint(10000, 50000))
        return f'{pp}_{kk}_{vv}_{rint}'

    def luo_kansio(nimi: str):
        dirspath = os.path.dirname(__file__) + '\\subdirs'

        # tarkista onko kansio jo olemassa
        if onko_hakemisto_olemassa(dirspath, nimi):

            # Tämä looppaa niin kauan kunnes nimi_generaattorin nimi ei ole olemassa.
            while True:
                # luo kansio satunaisella nimellä
                rand_dir_name = nimi_genraattori()

                if not onko_hakemisto_olemassa(dirspath, rand_dir_name):
                    os.mkdir(dirspath+'\\'+rand_dir_name)
                    print(f'Olet jo luonut kansion nimellä: {nimi}')
                    print(f'Luotiin kansio nimellä: {rand_dir_name}')
                    break
        else:
            # luo kansio annetulla nimellä
            os.mkdir(dirspath+'\\'+nimi)
            print(f'Luotiin kansio nimellä: {nimi}')

    while True:
        print('\nValitse yksi:' +
            '\n1) Luo kansio satunnaisella nimellä' +
            '\n2) Luo kansio nimellä' +
            '\n3) Tarkista montako kansiota on luotu' +
            '\n4) Poistu')

        toiminto = input('\nSyötä toiminto: ').strip()

        if toiminto == '1':
            luo_kansio(nimi_genraattori())

        elif toiminto == '2':
            nimi = input('\nSyötä luotavan kansion nimi: ').strip()
            luo_kansio(nimi)

        elif toiminto == '3':
            print(f'\nOlet luonut {kansio_kpl_maara()} kansiota.')

        elif toiminto == '4':
            print('\nKiitos ohjelman käytöstä.')
            break


if __name__ == "__main__":
    main()