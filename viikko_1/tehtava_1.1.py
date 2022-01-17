# TEHTÄVÄ 1.1

# -Kysyy käyttäjän nimeä ja vastaa sitten Hello "nimi"!
# -Muista lisätä koodin kommentit jotka selittävät mitä ohjelma tekee.

def main():
    # syötä arvo name muuttujalle
    name = input("Hei, syötä oma nimesi: ")
    # tervehdi
    print("Hello " + name + "!")


# kutsuu pääohjelman
if __name__ == "__main__": 
    main()