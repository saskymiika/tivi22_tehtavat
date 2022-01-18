# Tehtävä 2.3

# Tee ohjelma, joka hyödyntää if-rakennetta. Ohjelma kysyy käyttäjältä kolme lukua ja laskee niiden summan. Jos kaikki kolme ovat samoja, tulostetaan lukujen summa kerrottuna kolmella.

# Muussa tapauksessa tulostetaan niiden summa.
# Esimerkiksi, jos käyttäjä antaa ohjelmalle seuraavat kolmen lukua:
# 1, 2 ja 3 saadaan tulokseksi 6, koska 1 + 2 + 3 = 6 ja luvut eivät ole samoja, joten niitä ei kerrota kolmella.
# Jos käyttäjä syöttää 4, 4 ja 4 saadaan tulokseksi 36, koska (4+4+4) * 3 = 36
# Lisää ohjelman loppuun seuraava viesti käyttäjälle: "Kiitos ohjelman käytöstä."
# - Muista lisätä koodin kommentit jotka selittävät mitä ohjelma tekee.


# funtion joka kysyy kolmea lukua ja palauttaa ne yhteen arrayhin
def kysy_kolmea_lukua():
    return [input("luku 1: "), input("luku 2: "), input("luku 3: ")]


def main():
    print('Ole hyvä ja syötä kulme lukuarvoa.')
    luvut = kysy_kolmea_lukua() 

    # tarkista että luvut ovat numeroita
    if not(luvut[0].isdigit()) and not(luvut[1].isdigit()) and not(luvut[2].isdigit()):
        print("Luvut eivät kelpaa, ole hyvä ja yritä uudelleen")
        return
    
    # vertaa lukuja, jos ovat kaikki samoja
    if luvut[0] == luvut[1] and luvut[0] == luvut[2]:
        print("luvut olivat kaikki samoja, lukujen summa kerrotaan kolmella")
        print((float(luvut[0]) + float(luvut[1]) + float(luvut[2])) * 3)
    else:
        print(float(luvut[0]) + float(luvut[1]) + float(luvut[2]))


if __name__ == "__main__":
    main()