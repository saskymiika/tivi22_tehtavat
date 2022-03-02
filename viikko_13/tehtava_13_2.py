"""
Tehtävä 13.2
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

import io, os


def main():
    path = os.path.dirname(__file__)

    with io.open(path+'\\nimi01.txt', 'r', encoding="utf-8") as f:
        rivi1 = f.read().split('\n')[0].strip()
        print('Tiedoston: nimi01.txt ensimmäinen rivi on:', rivi1)
        f.close()
        
    with io.open(path+'\\nimi02.txt', 'r', encoding="utf-8") as f:
        rivi1 = f.read().split('\n')[0].strip()
        print('Tiedoston: nimi02.txt ensimmäinen rivi on:', rivi1)
        f.close()
        
    with io.open(path+'\\nimi03.txt', 'r', encoding="utf-8") as f:
        rivi1 = f.read().split('\n')[0].strip()
        print('Tiedoston: nimi03.txt ensimmäinen rivi on:', rivi1)
        f.close()

    print('\nKiitos ohjelman käytöstä.')


if __name__ == "__main__":
    main()