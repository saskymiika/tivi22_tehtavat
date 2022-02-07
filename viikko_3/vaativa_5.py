"""
Viikko 3 vaativa tehtävä 5
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

# Teit aiemmissa tehtävissä palindromitehtävän. 

# Lisää nyt ohjelmaan valikkorakenne (while True), joka 

#   1. pyytää sanaa 
#   2. kysyy näytetäänkö sana vasemmalta oikealla ja ylhäältä alas vai oikealta vasemmalle ja alhaalta ylös. 
#   3. antaa mahdollisuuden lopettaa ohjelman suorituksen.


def main():
    # ensimmäinen silmukka, joka pyytää käyttäjältä sanaa
    while True:
        sana = input('Kirjoita jokin sana: ').strip()
        if not len(sana) > 0:
            print('siis...')
        else:
            break
    
    print('\nValitse tulostusjärjestys')
    # toinen silmukka joka kysyy sanan tulostusjärjestystä
    while True:
        jarjestys = input("\n1 = vasemmalta oikealla\n2 = oikealta vasemmalle\n3 = ylhäältä alas\n4 = alhaalta ylös\nEnter = ohjelman lopetus\n\nvalintasi: ").strip()

        # jos syöte on kokonaisluku
        if jarjestys.isdigit():
            # muuta int muotoon
            jarjestys = int(jarjestys)
            # jos valinta on jokin yllä määritellyistä
            if jarjestys < 5:
                
                # tarkista järjestys
                if jarjestys == 1:
                    print(sana)

                elif jarjestys == 2:
                    # käännä merkkijonon järjestys [::-1] avulla
                    print(sana[::-1]) 

                elif jarjestys == 3:
                    print(sana)
                    # tulosta sana for loopin sisällä...
                    for l in sana:
                        # ... sanan toisesta indeksistä alkaen
                        if sana.index(l) > 0:
                            print(l)
                else:
                    # sama kuin edellisessä elif blokissa, mutta käännä sana ensin toisinpäin
                    sana = sana[::-1]
                    print(sana)
                    for l in sana:
                        if sana.index(l) > 0:
                            print(l)
        
        # jos syöte on tyhjää
        elif len(jarjestys) < 1:
            break
                
    print("\nKiitos ohjelman käytöstä!")
    

if __name__ == "__main__":
    main()