"""
Tee ohjelma, joka pyytää käyttäjältä merkkijonosyötteen ja tarkistaa, onko merkkijono listassa olevissa merkkijonoissa.

Jos käyttäjän syöttämä merkkijono on listassa, se poistetaan.
Jos käyttäjän syöttämä merkkijono ei ole listassa se lisätään.
Jos käyttäjän syöttämä merkkijono on tyhjä, listan viimeinen alkio poistetaan.
Jos lista tyhjenee, ohjelman suoritus lopetetaan.
Jos käyttäjä syöttää merkkijonossa: “Lopeta”, ohjelman suoritus lopetetaan.

Hyödynnä listan ylläpidossa funktiota.

Esimerkkiajot:

Ajo01:

Eläintarhan eläimet: [‘kissa’, ‘vuohi’, ‘kissa’]
Syötä eläimen nimi: hevonen
1 eläin lisätty eläintarhaan.

Eläintarhan eläimet: [‘kissa’, ‘vuohi’, ‘kissa’, ‘hevonen’]
Syötä eläimen nimi: kissa
1 eläin poistettu eläintarhasta.

Eläintarhan eläimet: [‘vuohi’, ‘kissa’, ‘hevonen’]
Syötä eläimen nimi: kissa
1 eläin poistettu eläintarhasta.

Eläintarhan eläimet: [‘vuohi’, ‘hevonen’]
Syötä eläimen nimi: painetaan Enter-näppäintä = merkkijono on tyhjä
hevonen poistettu eläintarhasta.

"""

def main():
    # eläimet lista
    elaintarhan_elaimet = ["kissa", "vuohi", "kissa"]

    # ohjelman pää-loop
    while True:
        print("\nEläintarhan eläimet:", elaintarhan_elaimet)
        # elain syöte, strip() metodilla poistetaan turhat välit jos niitä tulee merkkijonoon joten "" == " "
        elain = input("Syötä eläimen nimi: ").strip()

        # tarkista syöte
        # jos elain löytyy listasta, poista elain
        if elain in elaintarhan_elaimet:
            elaintarhan_elaimet.pop( elaintarhan_elaimet.index(elain) )
            print("1 eläin poistettu eläintarhasta.")

        # jos elain ei ole listassa, lisää elain
        else:

            # jos syöte on tyhjä, poista listan viimeinen eläin
            if len(elain) < 1:

                # viimeinen eläin 
                print(elaintarhan_elaimet[len(elaintarhan_elaimet)-1], "poistettu eläintarhasta.")

                # poista viimeinen eläin pop() metodilla
                elaintarhan_elaimet.pop()
            
            #jos syöte ei ole tyhjä, eikä ole listassa
            else:

                # jos syöte == "Lopeta", lopeta ohjelma
                if elain.lower() == "lopeta":
                    print("Kiitos ohjelman käytöstä.")
                    break

                # jos syöte on normaali
                else:
                    elaintarhan_elaimet.append(elain)
                    print("1 eläin lisätty eläintarhaan.")


        # huom. tämän tulee olla siennetty oikeaan kohtaan
        # jos lista tulee tyhjäksi, lopeta ohjelma
        if len(elaintarhan_elaimet) < 1:
            print("Kiitos ohjelman käytöstä.")
            break



if __name__ == "__main__":
    main()