class Pankkitili:
    def __init__(self, saldo: float, omistaja: str):
        self.saldo = saldo
        self.omistaja = omistaja

    def print_meta(self):
        print(self.omistaja)
        print(self.saldo)