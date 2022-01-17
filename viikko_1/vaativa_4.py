# 4. Tehtävä:

# Tee ohjelma, jossa:
#   pyydetään käyttäjältä kolmen tuotteen hinnat (kahden desimaalin tarkkuudella) 
#   ja ne talletetaan muuttujiin kokonaislukuina.
# Kun käyttäjä on syöttänyt kolme hintaa, 
#   ohjelma tulostaa näytölle tekstin: “Ensimmäisen tuoteen hinta on pyöristettynä <hinta1> EUR, 
#   toisen tuotteen hinta on pyöristettynä <hinta2> EUR ja kolmannen tuotteen hinta on pyöristettynä <hinta3>.
# Lopuksi ohjelma tulostaa kaikkien tuotteiden yhteenlasketun hinnan kahdella 
#   merkitsevällä desimaalilla tulostaen näytölle tekstin: 
#   “Kaikkien tuotteiden yhteenlaskettu hinta kahden desimaalin tarkkuudella on <summa> EUR.”

# Ohjelman esimerkkiajo:
# Anna ensimmäisen huotteen hinta: 3.10
# Anna toisen tuotteen hinta: 4.75
# Anna kolmannen tuotteen hinta: 2.05
# Ensimmäisen tuoteen hinta on pyöristettynä 3 EUR, 
#   toisen tuotteen hinta on pyöristettynä 5 EUR ja kolmannen tuotteen hinta on pyöristettynä 2 EUR.
# Kaikkien tuotteiden yhteenlaskettu hinta kahden desimaalin tarkkuudella on 9.40 EUR.


def main():
    print("Ole hyvä ja anna kolmelle seuraavalle tuotteille hinta kahden desimaalin tarkkuudella")

    # syötä hinnat
    tuote1 = float(input("Anna ensimmäisen tuotteen hinta: "))
    tuote2 = float(input("Anna toisen tuotteen hinta: "))
    tuote3 = float(input("Anna kolmannen tuotteen hinta: "))

    # hinnat pyöristettynä
    print(
        "Ensimmäisen tuotteen hinta on pyöristettynä "+ str(round(tuote1)) + " EUR,",
        "toisen tuotteen hinta on pyöristettynä "+ str(round(tuote2)) + " EUR ja",
        "kolmannen tuotteen hinta on pyöristettynä "+ str(round(tuote3)) + " EUR."
    )

    # hinnat yhteensä
    print("Kaikkien tuotteiden yhteenlaskettu hinta kahden desimaalin tarkkuudella on "+ str(tuote1+tuote2+tuote3)+" EUR.")
    


if __name__ == "__main__":
    main()