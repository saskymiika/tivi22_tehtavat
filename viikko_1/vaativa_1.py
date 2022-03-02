# 1. Tehtävä:

# Muodosta kolme kokonaislukumuuttujaa, jotka saavat arvot 45, 75 ja 100.
# Tulosta muuttujien arvot näytölle ensimmäiselle riville välilyönnillä erotettuna. 
# Seuraavaksi tulosta muuttujat toiselle riville, ilman välilyöntejä. 
# Lopuksi tulosta muuttujat kolmannelle riville pilkulla ja "ja"-sanalla erotettuna.


def main():
    # kolme kokonaislukua
    kl_1, kl_2, kl_3 = 45, 75, 100

    # välilyönneillä erotettuna
    print(str(kl_1) + " " + str(kl_2) + " " + str(kl_3))
    # tai print(kl_1, kl_2, kl_3)

    # ilman välilyöntejä
    print(str(kl_1) + str(kl_2) + str(kl_3))

    # pilkulla ja ja-sanalla erotettuna
    print(str(kl_1) + ", " + str(kl_2) + " ja " + str(kl_3) )


# kutsu pää ohjelmaa
if __name__ == "__main__":
    main()