# TEHTÄVÄ 1.2

# Kirjoita Python ohjelma joka kysyy käyttäjän nimeä, lempikirjaa ja lempilaulua ja tulostaa sen jälkeen ruudulle:

# Hei "Nimi"!
# Lempikirjasi "Kirjan nimi" on minunkin mielestäni hyvä. Lempilaulusi "Laulun nimi" taas ei ole minulle tuttu, mutta kuuntelisin sen mielelläni.

def main():
    # kysy nimeä ja aseta nimi muuttujalle arvo, strip() poistaa tyhjät
    nimi = input("Hei, ole hyvä ja syötä nimesi: ").strip()

    # pakota nimi title() metodilla otsikko muotoon (alkamaa isolla etukirjaimella)
    nimi = nimi.title()

    # kysy lempikirjaa ja aseta lempi_kirja muuttujalle arvo
    lempi_kirja = input("Hei "+ nimi + "! Ole hyvä syötä lempikirjasi: ")

    # pakota otsikko muotoon...
    lempi_kirja = lempi_kirja.title()

    # kysy lempilaulua aseta lempi_laulu muuttujan arvo
    lempi_laulu = input(lempi_kirja + " on minunkin mielestäni hyvä. Ole hyvä syötä lempilaulusi: ")

    # pakota otsikko muotoon...
    lempi_laulu = lempi_laulu.title()

    print("Lempilaulusi \""+ lempi_laulu + "\" taas ei ole minulle tuttu.")


# kutsuu pääohjelman
if __name__ == "__main__": 
    main()