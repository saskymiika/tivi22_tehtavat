"""
Tehtävä 8.2
Miika Toivanen
miika.toivanen@edu.sasky.fi



A

Korjaa virhe seuraavasta koodista

#koodi tulostaa parilliset numerot 2-20

for numero in range[2, 21, 2]
    print(numero)



B

Täydennä seuraava koodi niin, että syntyy seuraava tulostus

sub_total = 0
temp = 0
for item in range( , ,):
    temp = sub_total
    sub_total += item
    print("sub_total:", temp, "+", item, "=",sub_total)
print("Total =", sub_total)

Tulostus:

sub_total: 0 + 25 = 25
sub_total: 25 + 30 = 55
sub_total: 55 + 35 = 90
sub_total: 90 + 40 = 130
sub_total: 130 + 45 = 175

Total = 175
"""


def main():
    print('A)')

    # Korjaa seuraavaa koodia:

    ## Koodi tulostaa parilliset numerot 2-20
    print('Tulosta parilliset numerot 2-20\n')

    # for numero in range[2, 21, 2]
    #     print(numero)

    # range-metodin parametrien arvot tulee kirjoittaa normaalisulkeisiin (), eikä hakasulkeisiin []
    # for-lauseen lopusta puuttuu kaksoipiste ":"

    # Korjattu koodi:
    for numero in range(2, 21, 2):
        print(numero)

    # Tehtävä B
    print('\nB)')
    print('Tulostus:\n')
    

    # Jos aloitetaan 25, ja loopataan 50 asti...
    # 1. Jos step on 5, niin ekalla kierroksella item-muuttujan arvo on 25
    # 2. Seuraavalla kierroksella item on 25 + step, eli 30.
    #    Näin sub_total on 25 + 30, eli 55.
    # 3. Seuraavalla kierroksella item on 30+5, eli 35, joka lisätää sub_total:n, eli sub_total on 55.
    #... Jatkamme tätä looppia numero 50 saakka, ja niin saamme oikean tulostuksen aikaan.

    sub_total = 0
    temp = 0
    for item in range(25, 50, 5):
        temp = sub_total
        sub_total += item
        print("sub_total:", temp, "+", item, "=", sub_total)
    print("\nTotal =", sub_total)


if __name__ == "__main__":
    main()