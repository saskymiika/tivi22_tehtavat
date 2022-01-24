# TEHTÄVÄ 1.1

# -Kysyy käyttäjän nimeä ja vastaa sitten Hello "nimi"!
# -Muista lisätä koodin kommentit jotka selittävät mitä ohjelma tekee.

def main():
    # syötä arvo name muuttujalle, strip() metodi poistaa tyhjät edestä ja takaa
    nimi = input("Hei, syötä oma nimesi: ").strip()

    # pakota nimi otsikko muotoon
    nimi = nimi.title()

    # tervehdi
    print("Hello " + nimi + "!")


# kutsuu pääohjelman
if __name__ == "__main__": 
    main()