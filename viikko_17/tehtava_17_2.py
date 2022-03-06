"""
Tehtävä 17.2
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

from pankkitili import Pankkitili

def main():
    pekan_tili  = Pankkitili(100, 'Pekka Python')
    pirjon_tili = Pankkitili(20000, 'Pirjo Pythonen')

    pekan_tili.saldo += 900
    pirjon_tili.saldo += 10000

    print(pekan_tili.saldo)
    print(pirjon_tili.saldo)


if __name__ == "__main__":
    main()
