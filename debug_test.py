
def main():
    
    #Kysytään käyttäjän pituus ja paino
    pituus = int(input("Hei! Olisitko hyvä ja kertoisit pituutesi senttimetreinä?: "))
    paino = int(input("Jos seuraavaksi kertoisit painosi kiloina?: "))
    #Lasketaan pituus2 ja pyöristetään se 2 desimaalin tarkkuudella.
    nelio = round(pituus * pituus,2)
    #Jaetaan pituus2 pituudella ja jataan se 10000, jolloin saadaan luku esiintymään oikein. Tämän jälkeen pyöristetään luku 2 desimaalin tarkkuudella.
    indeksi = round(nelio / 10000,2)
    #Jaetaan paino pituudella ja pyöristetään luku 2 desimaalin tarkkuudella
    vastaus = round(paino / indeksi,2)
    #Tulostetaan vastaus ja annetaan tiedot mihin taulukossa kuuluu.
    print (float(vastaus))
    
    #Painoindeksi taulukko ja toimintaohjeet.
    if vastaus >=18.5 and vastaus <=25:
        print("Painoindeksisi on normaali, jatka samaan malliin!")
    elif vastaus >=25 and vastaus <=30:
        print("Olet lievästi ylipainoinen, mutta epäilen sitä suuresti. Sanoisin että hyvin menee!")
    elif vastaus >=30 and vastaus <=35:
        print("Taulukon mukaaan merkittävä lihavuus. Tunti liikuntaa päivässä muuttaa tilannetta!")
    elif vastaus >=35 and vastaus <=40:
        print("Vaikea lihavuus. Suosittelen muuttamaan ruokavaliota sekä aloittamaan hitaasti pienen liikunnan. Älä Woltita, kävele kauppaan.")
    elif vastaus >=40:
        print("Sairaanloinen lihavuus. Suosittelen keskustelemaan lääkärin kanssa eri vaihtoehdoista miten saisit painoa putoamaan.")
    else:
        print("Olet alipainoinen, suosittelen että olet yhteydessä lääkäriin.")



if __name__ == "__main__":
    main()