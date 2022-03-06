"""
Tehtävä 18.1
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""


from time import sleep


class Pisinsana:
    def __init__(self):
        self.pelaajat = [input('Pelaaja 1 nimi: ').strip(), input('Pelaaja 2 nimi: ').strip()]

    def start(self):
        while True:
            sanat = [input(f'{self.pelaajat[0]}, syötä sana: ').strip(), 
            input(f'{self.pelaajat[1]}, syötä sana: ').strip()]

            print('\nMietitään...\n')
            sleep(2.4)

            if len(sanat[0]) == len(sanat[1]):
                print('Tasapeli!')
            elif len(sanat[0]) > len(sanat[1]):
                print(self.pelaajat[0]+' on voittaja!')
            else:
                print(self.pelaajat[1]+' on voittaja!')



            reset = input("\nPelaa uudelleen? (Y/n) ").strip()
            if reset == '' or reset.lower() == 'y':
                continue
            else:
                print('\nPeli lopetettu. Kiitos ohjelman käytöstä!')
                exit()
            




def main():
    game = Pisinsana()
    game.start()


if __name__ == "__main__":
    main()