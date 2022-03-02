"""
Tehtävä 8.3
Miika Toivanen
miika.toivanen@edu.sasky.fi


Luo kaksi listaa: Nisäkkäät ja linnut. Kumpaankin listaan ainakin viisi alkiota.

Yhdistä nämä kaksi listaa yhdeksi listaksi, jonka nimi on eläimet. Tulosta lista eläimet.

Järjestä lista eläimet aakkosjärjestykseen ja tulosta se.
Käännä lista, niin että aloitetaan aakkosten lopusta edetään kohti alkua ja tulosta se.

Listaesimerkit:
Linnut: "Harakka", "Naakka", "Punatulkku", "Joutsen", "Varis"
Nisäkkäät: "Jänis", "Kissa", "Koira", "Hevonen", "Susi"

Tulostus:
["Harakka" , "Naakka", "Punatulkku" , "Joutsen" , "Varis", "Jänis", "Kissa", "Koira", "Hevonen" , "Susi"]
["Harakka" , "Hevonen" , "Joutsen" , "Jänis" , "Kissa", "Koira", "Naakka", "Punatulkku" , "Susi", "Varis"]
["Varis", "Susi" , "Punatulkku" , "Naakka", "Koira", "Kissa", "Jänis", "Joutsen" , "Hevonen" , "Harakka"]
"""


def main():
    # Eläin listat nisäkkäistä ja linnuista
    nisakkaat = ["Jänis", "Kissa", "Koira", "Hevonen", "Susi"]
    linnut = ["Harakka", "Naakka", "Punatulkku", "Joutsen", "Varis"]

    # + operaattorilla voimme yhdistää kaksi listaa yhdeksi
    elaimet = nisakkaat + linnut
    print('Tulostus:')
    print(elaimet)

    # Voidaan käyttää myös listan metodia extend() listojen yhdistämiseen, mutta metodin tyyppi on Void, eli se ei palauta uuden listan arvoa.
    # vaan extend() metodi muuttaa sen listan, jolla sitä metodia käytetään, uuteksi pidennetyksi listaksi.
    # Esim: elaimet.extend(linnut)
    # elaimet == elaimet + linnut == True

    # listan sort()-metoilla järjestämme listan aakkosjärjestykseen a-ö, sillä lista koostuu merkkojonoista.
    # Jos reverse paramtrille on annettu arvo True, sort()-metodi palauttaa listan käänteisessä järjestyksessä, ö-a. 
    nisakkaat.sort(reverse=True)
    linnut.sort(reverse=True)

    # Tulostaa uudelleen järjestetyt listat.
    print(nisakkaat)
    print(linnut)


if __name__ == "__main__":
    main()