"""
Tehtävä 8.4
Miika Toivanen
miika.toivanen@edu.sasky.fi

Luo 20 numeron merkkijono esimerkiksi "01234567890123456789"
Muuta (cast) se listaksi
laske yhteen kaikkien numeroiden summa
tulosta lasku ja lopputulos
Vinkki: .join() auttaa laskun tulostamisessa(1+2+3+...)

Esimerkkiajo:

0+1+2+3+4+5+6+7+8+9+0+1+2+3+4+5+6+7+8+9=90

Kiitos ohjelman käytöstä.
"""


def main():
    # 20-merkkinen merkkijono
    numerot = "09128734650192837465"
    # Merkkijono listaksi
    numerotlista = list(numerot)
    # TAI
    # numerotlista = []
    # numerotlista[:0] = numerot

    # "+".join(lista) string.join() metodi yhdistää listan merkkijonoksi "+":n määrityksen mukaan
    # sum() funktio laskee listan kokonaislukujen summan
    # map() funktiolla muutamme listan toisenlaiseen muotoon
    # lambda funktiolla kirjoitamme funktion toiminnon yhdelle riville.
    # funktio palauttaa merkki:n int(kokonaislukuna)
    print(f'{"+".join(numerotlista)}={sum(map(lambda merkki: int(merkki), numerotlista))}')
    print('\nKiitos ohjelman käytöstä.')


if __name__ == "__main__":
    main()