# Vaativa 2

# Tee ohjelma, joka pyytää käyttäjältä luvun ja selvittää, onko se parillinen vai pariton. Hyödynnä tarkistuksessa funktiota ja jakojäännöstä.

def onko_parillinen(arvo: int) -> int:
    # palauttaa boolean arvon (True tai False) riippuen jakojäännöksestä
    return arvo % 2 == 0


def main():
    # syötä arvo luku-muuttujalle
    luku = input("Syötä kokonaisluku: ")
    
    # tarkista että käytetään kokonaislukua isidigt() metodilla
    if not(luku.isdigit()):
        print("Ole hyvä ja käytä kokonaislukua.")
        return

    # muuttaa lukuarvon INT muotoon
    luku = int(luku)

    # tarkista onko luku parillinen vai ei
    if onko_parillinen(luku):
        print("Syöttämäsi luku on parillinen.")
    else:
        print("Syöttämäsi luku on pariton")


if __name__ == "__main__":
    main()