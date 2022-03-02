"""
Tehtävä 12.2
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

import math


def main():
    # Jotenka, alkuluku on kokonaisluku joka on ainoastaan jaollinen yhdellä ja itsellään.
    while True:
        luku = input('\nSyötä kokonaisluku: ').strip()
        if luku.isdigit():
            luku = int(luku)
            break
        elif luku == '':
            exit()
    
    silmukka_laskuri = 1
    alku_luku = luku > 1

    for i in range(2, luku):
        # jos jakojäännös == 0
        if luku % i == 0:
            alku_luku = False
            break
        
        silmukka_laskuri += 1
    
    # Tulostetaan lopputulos
    if alku_luku:
        print(f'\n{luku}', "on alkuluku!")
    else:
        print(f'\n{luku}', "EI OLE alkuluku.")

    print("Silmukoiden kokonaismäärä:", silmukka_laskuri)
    print("Kiitos ohjelman käytöstä.")


if __name__ == "__main__":
    while True:
        main()