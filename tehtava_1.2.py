# TEHTÄVÄ 1.2

# Kirjoita Python ohjelma joka kysyy käyttäjän nimeä, lempikirjaa ja lempilaulua ja tulostaa sen jälkeen ruudulle:

# Hei "Nimi"!
# Lempikirjasi "Kirjan nimi" on minunkin mielestäni hyvä. Lempilaulusi "Laulun nimi" taas ei ole minulle tuttu, mutta kuuntelisin sen mielelläni.

def main():
    # kysy nimeä ja aseta nimi muuttujalle arvo
    nimi = input("Hei, ole hyvä ja syötä nimesi: ")

    #kysy lempikirjaa ja aseta lempi_kirja muuttujalle arvo
    lempi_kirja = input("Hei "+ nimi + "! Ole hyvä syötä lempikirjasi: ")

    # kysy lempilaulua aseta lempi_laulu muuttujan arvo
    lempi_laulu = input(lempi_kirja + " on minunkin mielestäni hyvä. Ole hyvä syötä lempilaulusi: ")

    print("Lempilaulusi \""+ lempi_laulu + "\" taas ei ole minulle tuttu.")


# kutsuu pääohjelman
if __name__ == "__main__": 
    main()