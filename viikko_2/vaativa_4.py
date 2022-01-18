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

def main():

    print("Painoindeksi laskuri")

    pituus = input("Syötä pituus (cm): ")
    paino = input("Syötä paino (kg): ")
    
    if not(pituus.isdigit()) and not(paino.isdigit()):
        print("Ole hyvä ja käytä numeroita")
        return

    # muuta float muotoon ja paino oikeaan yksikköön
    pituus = float(pituus)
    paino = float(paino) / 10


if __name__ == "__main__":
    main()