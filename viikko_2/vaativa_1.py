# Vaativa tehtävä 1

# Ohjelmoi yksinkertainen laskin, joka kysyy kaksi lukua ja sen jälkeen kysyy, mitä luvuille tehdään (1 =  lisäys (luku1 + luku2), 2 = vähennys (luku1 - luku2), 3 = kerto (luku1 * luku2) tai 4 = jako (luku1 / luku2).
#Lopuksi laskin laskee halutun laskutoimituksen.

#Ohjelman esimerkkiajo:

# Ajo1:
# Syötä ensimmäinen luku: 2
# Syötä toinen luku: 4
# Mitä luvuille tehdään? (1=lisäys, 2=vähennys, 3=kerto, 4=jako): 3
# Luku: 2 kertaa luku: 4 = 8
# Kiitos ohjelman käytöstä.


def main():
    print("YKSINKERTAINEN LASKIN")
    print(" + - * / ")
    print("Ole hyvä ja syötä kaksi lukuarvoa")

    # syötä kaksi lukuarvoa
    luku1 = input("luku 1: ")
    luku2 = input("luku 2: ")

    # tarkista syötteet
    if not(luku1.isdigit()) and not(luku2.isdigit()):
        print("Ole hyvä ja käytä numeroita lukuarvoina")
        return

    # laskutoimitusvaihtoehdot
    print("Kirjoita laskutoimituksen numero luvuille "+luku1+" "+luku2)
    print(" 1 = lisäys")
    print(" 2 = vähennys")
    print(" 3 = kerto")
    print(" 4 = jako")

    lt_numero = input("Laskutoimitus: ")

    # varmista että käyttää numeroa
    if not(lt_numero.isdigit()):
        print("Ole hyvä ja syötä kokonaislukua (1, 2, 3 tai 4)")
        return

    # TYHJÄÄ selkeyttämään asioita
    print(" ")

    # Tarkista laskutoimitusvaihtoehdot
    if int(lt_numero) == 1:
        print(luku1+" + "+luku2)
        print("=", float(luku1) + float(luku2))
    elif int(lt_numero) == 2:
        print(luku1+" - "+luku2)
        print("=", float(luku1)-float(luku2))
    elif int(lt_numero) == 3:
        print(luku1+" * "+luku2)
        print("=", float(luku1)*float(luku2))
    elif int(lt_numero) == 4:
        print(luku1+" / "+luku2)
        print("=", float(luku1)/float(luku2))
    else:
        print("Syöttämäsi numero ei täsmää annettuihin vaihtoehtoihin.")

    # TYHJÄÄ selkeyttämään asioita
    print(" ")

    print("Kiitos ohjelman käytöstä!")


if __name__ == "__main__":
    main()