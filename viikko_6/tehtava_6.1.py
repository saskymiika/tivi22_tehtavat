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
        # syötä luku ja strip() metodilla ota tyhjät pois edestä ja takaa
        luku = input("\nSyötä kokonaisluku,\npoistu valikosta syöttämällä tyhjä,\n-tai-\nlopeta ohjelma syöttämällä \"K\".\n\nSyötteesi: ").strip()

        # jos luku on kokonaisluku
        if luku.isdigit():
            lukulista.append(luku)
            print(lukulista)
        
        # jos luku on "k"
        elif luku.casefold() == "k":
            return "k"

        # hyppää ulos while-silmukasta jos luku on tyhjä
        elif len(luku) < 1:
            break

        # jos luku ei ole kelvollinen
        else:
            print("\nVIRHE! Käytä kokonaislukua!")


def kysy_valinta():
    while True:
        valinta = input("\nValitse seuraavista vaihtoehdoista\n\nL = Lukulista ja niiden summa\nS = Pelkkä summa\n\nValintasi: ")

        # tarkista että arvo on s tai l
        if valinta.casefold() == "s" or valinta.casefold() == "l":
            return valinta
        else:
            print("\nOle hyvä ja käytä 'L' tai 'S' -merkkiä")


def main():
    # lukulista
    lukulista = []

    while True:
        luku = kysy_lukua(lukulista)

        # jos luku:n arvo ei ole None, jos käyttäjä on syöttänyt "K", hyppää ulos silmukasta ja lopettaa ohjelman
        if luku != None:
            print("\nKiitos ohjelman käytöstä!")
            break

        # palauttaa arvon "S" tai "L"
        valinta = kysy_valinta()

        # muuttaa valinnan pieniksi kirjaimiksi ja vertaa arvoa
        if valinta.casefold() == "l":
            # tulosta lukulistan ja niiden summan
            print("\nLukulista:", lukulista)
            print("Lukujen summa:",sum(map(int, lukulista)))

        elif valinta.casefold() == "s":
            # tulostaa lululistan SUMMAN
            print("\nLukujen summa:",sum(map(int, lukulista)))

        # jos ei kumpikaan ehto täyty, ohjelma looppaa takaisin alkuun ja kysyy uudestaan syötettä    

    
if __name__ == "__main__":
    main()