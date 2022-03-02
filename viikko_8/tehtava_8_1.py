"""
Tehtävä 8.1
Miika Toivanen
miika.toivanen@edu.sasky.fi


Tee ohjelma joka tarkistaa löytyykö käyttäjän haluamaa maalisävyä varastosta.

Varastossa olevat maalisävyt määrittelet vain luomalla listan maaleista ohjelmaasi.

Tulosta aluksi "Varastosamme on seuraavia sävyjä: (Ja värit jokainen omalle rivilleen)" 
Kysy sitten käyttäjältä mitä maalia käyttäjä haluaisi ja palauta varastosta löytyy tai valitettavasti meillä ei ole juuri tuota sävyä.

Esimerkkiajo01:

varastossa = ["sininen", "punainen", "vihreä", "keltainen", "turkoosi"]

Ohjelma käynnistetään

Varastossamme on seuraavia sävyjä:
sininen
punainen
vihreä
keltainen 
turkoosi

Mitä väriä tarvitset?
SININEN
Varastosta löytyy.
Kiitos ohjelman käytöstä.



varastossa = ["sininen", "punainen", "vihreä", "keltainen", "turkoosi"]

Esimerkkiajo02:

Ohjelma käynnistetään

Varastossamme on seuraavia sävyjä:
sininen
punainen
vihreä
keltainen 
turkoosi

Mitä väriä tarvitset?
Kulta
Valitettavasti meiltä ei löydy juuri tuota sävyä.
Kiitos ohjelman käytöstä.
"""


def main():
    print('Ohjelma käynnistetään.')
    # Värit lista.
    varit = ["sininen", "punainen", "vihreä", "keltainen", "turkoosi"]

    print('\nVarastossamme on seuraavia sävyjä:')
    # Tulostaa jokaisen värin 
    for v in varit:
        print(v.lower())

    # Otetaan inputista ythjät pois ja muutetaan pikkukirjaimiksi.
    vari = input('\nMitä väriä tarvitset?\n> ').strip().lower()

    if vari in varit:
        print(f'Varastosta löytyy.\n{vari.upper()}')

    else:
        print('Valitettavasti meiltä ei löydy juuri tuota sävyä.')

    print('\nKiitos ohjelman käytöstä.')


if __name__ == "__main__":
    main()