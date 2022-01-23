
# Tehtävä 3.4

# Lisää edelliseen ohjelmaan toiminto, jossa ohjelma kysyy, montako arvosanaa käyttäjä aikoo syöttää. Lopuksi ohjelma laskee syötettyjen arvosanojen keskiarvon. Toteuta silmukka while-rakenteella.

def lisaa_arvosanat(lista, pituus):
    # li = listaindeksi
    li = 0
    
    # luuppaa annetun pituuden mukaan ja kysy arvosanoja, sekä lisää ne viitattuun listaan
    while li < pituus:
        arvosana = input("Syötä arvosana: ")

        #tarkista että syötetään numero
        if not arvosana.isdigit():
            print("Ole hyvä ja käytä kokonaislukua.")
            return

        # lisää arvosana listaan kokonaislukuna
        lista.append(int(arvosana))

        # increment loop index
        li += 1


def main():
    print("Syötä arvosanoja yksi kerrallaan.")

    arvosanojen_maara = input("Montako arvosanaa tahdot syöttää? ")

    if not arvosanojen_maara.isdigit():
        print("Ole hyvä ja anna kokonaisluku.")
        return

    # arvosanat lista, lisää tänne kaikki arvosanat
    arvosanat = []
    
    # itse tehty apufunktio, kysyy 5 kertaa arvosanaa ja lisää ne arvosanat-listaan
    lisaa_arvosanat(arvosanat, int(arvosanojen_maara))

    # laskee arvosanojen keskiarvon
    keskiarvo = sum(arvosanat) / len(arvosanat)

    print("Syötettyjen arvosanojen keskiarvo on:",'%.1f' % keskiarvo)
    print("Kiitos ohjelman käytöstä!")


if __name__ == "__main__":
    main()