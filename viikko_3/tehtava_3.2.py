"""
Tehtävä 3.2
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

# Tee ohjelma, joka pyytää käyttäjältä sarjan aloitus- ja lopeusnumeron ja tulostaa sen jälkeen while-toistorakenteella arvot jonoon seuraavan esimerkin mukaisesti:

# Anna sarjan aloitusnumero: 3
# Anna sarjan lopetusnumero: 12
# Luvut while-rakenteella listattuna ovat:

# 3
# ...
# 12

# Kiitos ohjelman käytöstä.

def main():
    # kysy aloitusnumeroa
    a_num = input("Anna sarjan aloitusnumero: ")

    # tarkista että digit...
    if not a_num.isdigit():
        print("Ole hyvä käytä numeroita.")
        return
    
    # kysy lopetusnumeroa
    l_num = input("Anna sarjan lopetusnumero: ")

    # tarkista että ovat digit...
    if not l_num.isdigit():
        print("Ole hyvä käytä numeroita.")
        return

    # muuta merkit kokonaisluvuiksi
    a_num = int(a_num)
    l_num = int(l_num)

    print("Luvut while-rakenteella listattuna ovat:")

    # aloitusluvusta lopetuslukuun while loopilla
    while a_num < l_num+1:
        print(a_num)
        a_num += 1

    print("Kiitos ohjelman käytöstä!")


if __name__ == "__main__":
    main()