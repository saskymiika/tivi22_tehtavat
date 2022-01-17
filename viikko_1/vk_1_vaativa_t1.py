# 1. Tehtävä:

# Muodosta kolme kokonaislukumuuttujaa, jotka saavat arvot 45, 75 ja 100.
# Tulosta muuttujien arvot näytölle ensimmäiselle riville välilyönnillä erotettuna. 
# Seuraavaksi tulosta muuttujat toiselle riville, ilman välilyöntejä. 
# Lopuksi tulosta muuttujat kolmannelle riville pilkulla ja "ja"-sanalla erotettuna.

# kolme kokonaislukua
kl_1, kl_2, kl_3 = 45, 75, 100


def main():
    # välilyönneillä erotettuna
    rivi_1 = str(kl_1) + " " + str(kl_2) + " " + str(kl_3)
    print(rivi_1)
    # tai
    # print(kl_1, kl_2, kl_3)

    # ilman välilyöntejä
    rivi_2 = rivi_1.replace(" ", "")
    print(rivi_2)

    # pilkulla ja ja-sanalla erotettuna
    rivi_3 = str(kl_1) + ", " + str(kl_2) + " ja " + str(kl_3) 
    print(rivi_3)


# kutsu pää ohjelmaa
if __name__ == "__main__":
    main()