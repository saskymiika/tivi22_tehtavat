"""
Tehtävä 18.2
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""


from random import randint
from time import sleep


class KiviPaperiSakset:
    def __init__(self):
        self

    def valitse_kps(self):
        print('\nSyötä numero.\n1) Kivi\n2) Sakset\n3) Paperi\n')
        while True:
            valinta = input('==> ')
            if valinta.isdigit():
                if int(valinta) >= 3:
                    valinta = '3'
                elif int(valinta) <= 1:
                    valinta = '1'
                return valinta

    def ksp(self, num: str):
        kps = {
            '1': 'Kivi',
            '2': 'Sakset',
            '3': 'Paperi'
        }
        return kps[num]


    def start(self):
        while True:
            print('\nVastustaja valitsee kivi, sakset tai paperi...')
            sleep(1.2)
            tietokone = self.ksp(str(randint(1, 3)))
            print('Valinta tehty!')
            mina = self.ksp(self.valitse_kps())
            print(f'Valintasi: {mina}. Katsotaan...')
            sleep(1.2)

            if tietokone == 'Paperi' and mina == 'Kivi':
                print('\nHävisit! Paperi voittaa kiven!')
            elif tietokone == 'Kivi' and mina == 'Paperi':
                print('\nVoitit! Paperi voittaa kiven!')

            elif tietokone == 'Sakset' and mina == 'Paperi':
                print('\nHävisit! Sakset voittaa Paperin!')
            elif tietokone == 'Paperi' and mina == 'Sakset':
                print('\nVoitit! Sakset voittaa Paperin!')

            elif tietokone == 'Kivi' and mina == 'Sakset':
                print('\nHävisit! Kivi voittaa Sakset!')
            elif tietokone == 'Paperi' and mina == 'Sakset':
                print('\nVoitit! Kivi voittaa Sakset!')

            elif tietokone == mina:
                print(f'\nTasapeli! {tietokone} - {mina}')


            reset = input("\nPelaa uudelleen? (Y/n) ").strip()
            if reset == '' or reset.lower() == 'y':
                continue
            else:
                print('\nPeli lopetettu. Kiitos ohjelman käytöstä!')
                exit()
            




def main():
    game = KiviPaperiSakset()
    game.start()


if __name__ == "__main__":
    main()