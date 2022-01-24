"""
Viikon 6, projektitehtävä
Katso viikon projektitehtävänanto tästä linkistä.

Tee ohjelma joka kysyy käyttäjältä lukuja ja tulostaa lopuksi joko kaikki luvat ja niiden summan tai pelkän summan. Käyttäjältä kysytään ensi raporttityyppi

L = lukulista ja Summa

S = PELKKÄ SUMMA

Valinnan jälkeen kysytään kokonaisluku tai k. Uutta lukua kysytään kunnes käyttäjä antaa k. Käyttäjän virheellisistä syötteitä pitää antaa järkevä palaute.
Tee ensin vuokaavio ja testaussuunnitelma. 

Sen jälkeen kirjoita koodi ja testaa se oman testaussuunnitelmasi mukaisesti.
Tämän jälkeen lähetä koodisi ryhmäsi jäsenille jotka testaavat sen oman testaussuunnitelmansa mukaisesti ja raportoivat sinulle mahdolliset ongelmat. Korjaa mahdolliset ongelmat ja lähetä koodi uudelleen tarkistettavaksi.
Ryhmän jäsenet tarkistavat myös onko koodi tyylioppaan mukaista.

Lopuksi palauta tiedostoina testaussuunnitelma, vuokaavio, koodi sekä ainakin yhden ryhmäsi jäsenen kommentit.
"""

from typing import List

def kysy_lukua(lukulista: List) -> None:
    while True:
        # syötä luku ja ota tyhjät pois (edestä ja takaa)
        luku = input("\nOle hyvä ja syötä kokonaisluku. Poistu syöttämällä tyhjän.\nlukusi: ").strip()

        # jos numero JA lyhyempi kuin 2 () eli 1
        if luku.isdigit():
            lukulista.append(luku)
            print(lukulista)

        # hyppää ulos while-silmukasta jos luku on tyhjä
        elif len(luku) < 1:
            break

        # jos luku ei ole kelvollinen
        else:
            print("\nOle hyvä ja käytä kokonaislukua.")


def kysy_valinta():
    while True:
        valinta = input("\nOle hyvä ja valitse seuraavista vaihtoehdoista\n\nL = Tulosta lukulista ja niiden summa\nS = pelkkä summa\n\nValintasi: ")



def main():
    # lukulista
    lukulista = []

    while True:
        kysy_lukua(lukulista)



        print(valinta, lukulista)
        break
    


if __name__ == "__main__":
    main()