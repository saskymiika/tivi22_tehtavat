"""
Tehtävä 7.3
Miika Toivanen
miika.toivanen@edu.sasky.fi


Kirjoita funktio, joka ottaa kolme argumenttia. Merkkijonon ja kaksi kokonaislukua. 

1. Funktio muuttaa annetun merkkijonon kokonaisluvuksi, laskee kaikki kolme yhteen ja palauttaa (return) pääohjelmalle saadun lopputuloksen kokonaislukuna.
2. Määritä pääohjelmassa kaksi muuttujaa ja niille kokonaislukuarvot. 
3. Kysy käyttäjän ikää.
4. Kutsu tekemääsi funktiota näillä kolmella argumentilla.
5. Printtaa pääohjelmassa lopuksi ruudulle yhteenlaskun tulos.
"""


def kolmen_luvun_summa(merkkijononi: str, luku1: int, luku2: int) -> int:
    # Muuta merkkijono numeroksi ja laskee kaikki kokonaisluvut yhteen.
    return int(merkkijononi) + luku1 + luku2


def main():
    # Valmiit kokonaisluvut
    luku1 = 10
    luku2 = 16

    # Syötä käyttäjän ikä inputilla.
    while True:
        kayttajan_ika = input("Syötä ikäsi: ").strip()
        if kayttajan_ika.isdigit():
            break
        else:
            print("Käytä kokonaislukua.")

    # tulosta kolemn luvun summa itsetehdyllä funktion avulla.
    print("Kolmen luvun summa:", kolmen_luvun_summa(kayttajan_ika, luku1, luku2))


if __name__ == "__main__":
    main()