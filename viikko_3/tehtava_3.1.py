# Tehtävä 3.1

# Käytä sisäkkäistä if-rakennetta ja tee ohjelma, joka pyytää käyttäjää kirjoittamaan kissa, koira, lehmä tai lammas ja tulostaa sitten tämän eläimen kutsuhuudon. Vertaa ensin sanojen alkukirjaimia ja sen jälkeen sisennetyssä ehtolauseessa tarkistat sanan toisen kirjaimen perusteella onko esim. k-kirjaimella alkava eläin kissa vai koira.

# Jos käyttäjä on syöttänyt muuta kuin jonkun yllä mainituista loistavista eläinlajeista, tulee sinun kertoa käyttäjälle, että hän ei osaa.

# - Muista lisätä koodin kommentit jotka selittävät mitä ohjelma tekee.


def main():
    elain = input('Syötä yksi näistä eläimistä: kissa, koira, lehmä tai lammas: ')
    
    # tarkista että käyttäjä on kirjoittanut oikean eläimen
    # ainoat sallitut eläimet
    sallitut_elaimet = ['kissa', 'koira', 'lehmä', 'lammas']

    # in operaattorilla tarkistetaan jos tavara löytyy yllä määritetystä listasta
    if elain.lower() not in sallitut_elaimet:
        print("Et oikeen osaa. Kirjoita: kissa, koira, lehmä tai lammas.")
        return 


    # vertaa elaimen alkukirjainta
    if elain[0].lower() == 'k':
        # vertaa elaimen toista kirjainta 
        if elain[1].lower() == 'i':
            print('MIAU!')
        else:
            print('WUH WUH!')
            

    elif elain[0].lower() == 'l':
        # vertaa elaimen toista kirjainta
        if elain[1].lower() == 'e':
            print('AMMUU!')
        else:
            print('MÄÄÄ!')
            

if __name__ == "__main__":
    main()