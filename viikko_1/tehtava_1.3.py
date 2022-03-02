# TEHTÄVÄ 1.3

# Pythonissa on olemassa valmisfunktio, joka kertoo muuttujan tyypin. 
# Käytä sitä ja tee ohjelma, joko tulostaa seuraavien muuttujien tyypit 

# ika = "25"
# nimi = "Liisa"
# kengan_koko = 17
# muistathan = "1"+"1"

ika = "25"
nimi = "Liisa"
kengan_koko = 17
muistathan = "1" + "1"


def main():
    # muuttujan "ika" -tyyppi
    print("muuttujan \"ika\" tyyppi", type(ika))

    # muuttujan "nimi" tyyppi
    print("muuttujan \"nimi\" tyyppi",  type(nimi))

    # muuttujan "kengan_koko" tyyppi
    print("muuttujan \"kengan_koko\" tyyppi", type(kengan_koko))

    # muuttujan "muistathan" tyyppi
    print("muuttujan \"muistathan\" tyyppi", type(muistathan)) 


# kutsuu pääohjelman
if __name__ == "__main__": 
    main()