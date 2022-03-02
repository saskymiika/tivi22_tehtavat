"""
Tehtävä 11.1
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

import math

def main():
    luvut = []
    while True:
        luku = input(f'Syötä luku{len(luvut)+1}: ').strip()
        if luku.isdigit():
            luvut.append(int(luku))

        if len(luvut) >= 2:
            break

    # Suurin jakaja, on jakolaskuntulos pyöristettynä alas.
    print(f'Lukujen {luvut[0]} ja {luvut[1]} suurin mahdollinen jakaja on:', math.floor(luvut[0] / luvut[1]))


if __name__ == "__main__":
    main()