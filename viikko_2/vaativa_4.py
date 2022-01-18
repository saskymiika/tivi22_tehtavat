# 4. Tehtävä: (haastava)

# Tee ohjelma, joka laskee syötetyillä luvuilla henkilön painoindeksin.
# Ohjelma ilmoittaa käyttäjälle painoindeksin sekä antaa tietoa, miten siihen tulisi suhtautua.

# Painoindeksiä laskettaessa, paino jaetaan pituuden "neliöllä" (pituus2 eli pituus × pituus). "Neliöinnissä" eli toiseen potenssiin korottamisessa luku kerrotaan itsellään, esimerkiksi 32 = 3 x 3.
# Painoindeksilaskussa paino ilmaistaan kiloina ja pituus metreinä. Esimerkiksi 175-senttisen ja 80 kiloa painavan henkilön painoindeksi lasketaan seuraavasti:
# 80 : 1,7522 = 80 : (1,75 × 1,75) = 80 : 3,06 = 26,1.

# Taulukko tulkintaan:

# 18,5 - 25: normaali painoindeksi
# 25–30: ylipaino eli lievä lihavuus
# 30–35: merkittävä lihavuus
# 35–40: vaikea lihavuus
# Yli 40: sairaalloinen lihavuus.

# painoindeksi = paino / (pituus * pituus)

from math import pow

def main():
    print("Painoindeksi laskuri")

    pituus = input("Syötä pituus (cm): ")
    paino = input("Syötä paino (kg): ")
    
    if not(pituus.isdigit()) and not(paino.isdigit()):
        print("Ole hyvä ja käytä numeroita")
        return

    # muuta float muotoon ja paino oikeaan yksikköön
    pituus = float(pituus) / 100 # senteistä metreiksi
    paino = float(paino)

    # float kahden desimaalin tarkkuudella 
    # voi käyttää myös (p_indeksi = '%.2f' % p_indeksi) format() metodin sijaan
    # format() metodi palauttaa arvon stringinä
    p_indeksi = format(paino / pow(pituus, 2), ".2f")

    # print("painoindeksi:", "%.2f" % p_indeksi)
    print("Painoindeksi:", p_indeksi)

    # muuta p_indeksi takaisin floatiksi
    p_indeksi = float(p_indeksi)

    # vertaa p_indeksiä taulukkoon
    if p_indeksi >= 18.5 and p_indeksi < 25:
        print("Normaali painoindeksi.")
    elif p_indeksi >= 25 and p_indeksi < 30:
        print("Ylipaino eli lievä lihavuus.")
    elif p_indeksi >= 30 and p_indeksi < 35:
        print("Merkittävä lihavuus.")
    elif p_indeksi >= 35 and p_indeksi < 40:
        print("Vaikea lihavuus.")
    elif p_indeksi >= 40 and p_indeksi < 50:
        print("sairaalloinen lihavuus.")


if __name__ == "__main__":
    main()