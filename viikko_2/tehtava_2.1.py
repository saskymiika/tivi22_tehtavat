"""
Tehtävä 2.1
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

# Tee ohjelma joka kysyy käyttäjän ikää ja sen mukaan minkä arvon käyttäjä antaa vastaa.

# Alle 12: Ohjelma sanoo "Olet vielä lapsi".
# 12-18: Ohjelma sanoo "Olet nuori"
# 18 tai enemmän "Olet aikuinen"

def main():
    # syötä arvo muuttujalle ika
    ika = input("Kuinka vanha olet? ")

    # tarkista että annettu arvo on numero/kokonaisluku isdigit() metodilla
    if ika.isdigit():
        # jos alle 12
        if int(ika) < 12:
            print("Olet vielä lapsi")
        # jos alle 18 (mutta 12 tai enem.)
        elif int(ika) < 18:
            print("Olet nuori")
        # jos 18 tai enemmän
        else:
            print("Olet aikuinen")
    else:
        print("Ole hyvä ja käytä kokonaislukua.")
        

if __name__ == "__main__":
    main()