# Tee ohjelma joka kysyy käyttäjän ikää ja sen mukaan minkä arvon käyttäjä antaa vastaa.

# Alle 12: Ohjelma sanoo "Olet vielä lapsi".
# 12-18: Ohjelma sanoo "Olet nuori"
# 18 tai enemmän "Olet aikuinen"

def main():
    # kysy ikää
    ika = input("Kuinka vanha olet? ")

    # tarkista että annettu arvo on numero
    if ika.isdigit():
        if int(ika) < 12:
            print("Olet vielä lapsi")
        elif int(ika) < 18:
            print("Olet nuori")
        else:
            print("Olet aikuinen")
    else:
        print("Ole hyvä ja käytä numeroarvoa")
        


if __name__ == "__main__":
    main()