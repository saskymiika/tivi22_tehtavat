"""
Tehtävä 13.4
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

import re


def main():
    
    elintarvikehakemisto = {'Leipä':2.26, 'Kaurajuoma':3.62, 'Suklaa':1.59}
    
    try:
        tuote = input('Syötä tuotteen nimi, jonka hintaa muutetaan: ').strip()

        if elintarvikehakemisto.get(tuote) == None:
            raise Exception(f'Tuotetta {tuote} ei ole!')
        else:
            hinta = input('Anna uusi hinta: ').strip()

            if len(hinta) == 0:
                raise Exception(f'Et antanut uutta hintaa tuotteelle {tuote}!')

            m = re.match(r'\b\d+\.\d+|\d+', hinta)
            if m == None or hinta.isalpha():
                raise Exception(f'Annoit viallisen hinnan tuotteelle {tuote}!')

            hinta = float(hinta[m.start():m.end()])

            elintarvikehakemisto[tuote] = hinta
            print(f'Tuotteen {tuote} uusi hinta on: {hinta}')

    except Exception as e:
        print('%s' % e)

    print('Kiitos ohjelman käytöstä.')


if __name__ == "__main__":
    main()