# 1. Tehtävä:

# Muodosta kolme kokonaislukumuuttujaa, jotka saavat arvot 45, 75 ja 100.
# Tulosta muuttujien arvot näytölle ensimmäiselle riville välilyönnillä erotettuna. 
# Seuraavaksi tulosta muuttujat toiselle riville, ilman välilyöntejä. 
# Lopuksi tulosta muuttujat kolmannelle riville pilkulla ja "ja"-sanalla erotettuna.

# kolme kokonaislukua
kl_1, kl_2, kl_3 = 45, 75, "tämä tulee ennen sataa, kun ulkona ei sada! "+str(100)+"."


def main():
    # välilyönneillä erotettuna
    rivi_1 = str(kl_1) + " " + str(kl_2) + " " + str(kl_3)
    print(rivi_1)
    # tai
    # print(kl_1, kl_2, kl_3)

    # ilman välilyöntejä
    rivi_2 = str(kl_1) + str(kl_2) + str(kl_3)
    print(rivi_2)

    # pilkulla ja ja-sanalla erotettuna
    rivi_3 = str(kl_1) + ", " + str(kl_2) + " ja " + str(kl_3) 
    print(rivi_3)


# kutsu pää ohjelmaa
if __name__ == "__main__":
    main()


# Tehtävä 2

# Lisää edellisen tehtävän muuttujan 100 eteen lause välilyönneillä erotettuna: 
# "tämä tulee ennen sataa, kun ulkona ei sada!"


# 3. Tehtävä: 

# Tallenna muuttujaan luku1 arvo 41 ja muuttujaan luku2 arvo 4. Tulosta näytölle ensimmäiselle riville jakolasku luku1 jaettuna luku2. Tulosta toiselle riville jakolaskun jakojäännös. Pythonissa jakojäännös laskuoperaattori on %-merkki. 

# Ohjelman esimerkkiajo:
# Jakolaskun tulos on: 10.25
# Jakolaskun jakojäännös on: 1
