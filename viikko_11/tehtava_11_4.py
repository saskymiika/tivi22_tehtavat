"""
Tehtävä 11.4
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

import sys, os


def main():
    # käyttöjärjestelmä
    print('\nKäyttöjärjestelmä on:', sys.platform)
    # hakemisto
    print('\nTämän hetkinen hakemisto:')
    curr_dir = os.path.dirname(__file__)

    print(curr_dir)
    dirname = input('\nMinkä nimisen hakemiston luon? ').strip()

    os.mkdir(curr_dir+'\\'+dirname)
    print(f'\nLuotu uusi hakemisto: {dirname}')
    print('\nKiitos ohjelman käytöstä.')


if __name__ == "__main__":
    main()