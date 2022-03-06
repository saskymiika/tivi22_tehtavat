class Lemmikki:
    def __init__(self, nimi: str, laji: str, syntymavuosi: int):
        self.nimi = nimi
        self.laji = laji
        self.syntymavuosi = syntymavuosi
        print('Uusi lemmikki lisätty')

    def call(self):
        print(self.nimi)
        print(self.laji)
        print(self.syntymavuosi)