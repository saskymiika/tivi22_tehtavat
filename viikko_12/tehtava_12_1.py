"""
Tehtävä 12.1
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

import re
from math import inf


def main():
    # Palauttaa boolean arvon onko num on float1 ja float2 välissä
    def in_btw(num, float1, float2):
        return num >= float1 and num < float2

    while True:
        kg = input('\nSyötä paino (kiloissa): ').strip()
        m1 = re.search(r"\b\d+\.\d+|\d+", kg) 
        if m1 == None:
            continue

        kg = kg[m1.start():m1.end()]

        m = input('\nSyötä pituus (metreissä): ').strip()
        m2 = re.search(r"\b\d+\.\d+|\d+", m) 
        if m2 == None:
            continue
        
        m = m[m2.start():m2.end()]

        # pi = painoindeksin arvo
        pi = float(kg) / float(m) ** 2

        if in_btw(pi, -inf, 16):
            print(f'\nPainoindeksi on {format(pi, ".1f")} > Vaikea alipaino')
        elif in_btw(pi, 16, 17):
            print(f'\nPainoindeksi on {format(pi, ".1f")} > Merkittävä alipaino')
        elif in_btw(pi, 17, 18.5):
            print(f'\nPainoindeksi on {format(pi, ".1f")} > Lievä alipaino')
        elif in_btw(pi, 18.5, 25):
            print(f'\nPainoindeksi on {format(pi, ".1f")} > Normaali paino')
        elif in_btw(pi, 25, 30):
            print(f'\nPainoindeksi on {format(pi, ".1f")} > Lievä ylipaino')
        elif in_btw(pi, 30, 35):
            print(f'\nPainoindeksi on {format(pi, ".1f")} > Merkittävä ylipaino')
        elif in_btw(pi, 35, 40):
            print(f'\nPainoindeksi on {format(pi, ".1f")} > Vaikea ylipaino')
        elif in_btw(pi, 40, inf):
            print(f'\nPainoindeksi on {format(pi, ".1f")} > Sairaalloinen ylipaino')

        print('\nKiitos ohjelman käytöstä.')
        break


if __name__ == "__main__":
    main()