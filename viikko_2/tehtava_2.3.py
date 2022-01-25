# Tehtävä 2.3

# Tee ohjelma, joka hyödyntää if-rakennetta. Ohjelma kysyy käyttäjältä kolme lukua ja laskee niiden summan. Jos kaikki kolme ovat samoja, tulostetaan lukujen summa kerrottuna kolmella.

# Muussa tapauksessa tulostetaan niiden summa.
# Esimerkiksi, jos käyttäjä antaa ohjelmalle seuraavat kolmen lukua:
# 1, 2 ja 3 saadaan tulokseksi 6, koska 1 + 2 + 3 = 6 ja luvut eivät ole samoja, joten niitä ei kerrota kolmella.
# Jos käyttäjä syöttää 4, 4 ja 4 saadaan tulokseksi 36, koska (4+4+4) * 3 = 36
# Lisää ohjelman loppuun seuraava viesti käyttäjälle: "Kiitos ohjelman käytöstä."
# - Muista lisätä koodin kommentit jotka selittävät mitä ohjelma tekee.


def main():
    print('Ole hyvä ja syötä kulme lukuarvoa.')
    luvut = [input("luku 1: "), input("luku 2: "), input("luku 3: ")]

    # tarkista että luvut ovat numeroita
    if not(luvut[0].isdigit()) and not(luvut[1].isdigit()) and not(luvut[2].isdigit()):
        print("Luvut eivät kelpaa, ole hyvä ja yritä uudelleen")
        return
    
    # lukujen summa float muodossa
    #   map() funktio muuttaa listan arvot int muotoon
    #   sum() laskee yhteen kaikki listan arvot
    summa = sum(map(int, luvut))

    # vertaa lukuja, jos ovat kaikki samoja
    if luvut[0] == luvut[1] == luvut[2]:
        print("\nLuvut olivat kaikki samoja, lukujen summa kerrotaan kolmella:")
        print("("+luvut[0]+" + "+luvut[1]+" + "+luvut[2]+ ") * 3 =", summa * 3 )
    else:
        print("\nLuvut eivät olleet samoja, lukujen summa:")
        print(luvut[0]+" + "+luvut[1]+" + "+luvut[2]+" =",summa)


if __name__ == "__main__":
    main()