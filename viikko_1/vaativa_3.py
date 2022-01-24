# 3. Tehtävä: 

# Tallenna muuttujaan luku1 arvo 41 ja muuttujaan luku2 arvo 4. 
# Tulosta näytölle ensimmäiselle riville jakolasku luku1 jaettuna luku2. 
# Tulosta toiselle riville jakolaskun jakojäännös. 
# Pythonissa jakojäännös laskuoperaattori on %-merkki. 

# Ohjelman esimerkkiajo:
# Jakolaskun tulos on: 10.25
# Jakolaskun jakojäännös on: 1

# muuttujat
luku1, luku2 = 41, 4

def main():
    # jakolasku
    print("Jakolaskun tulos on:", luku1 / luku2)

    # jakojäännös
    print("Jakolaskun jakojäännös on:", luku1 % luku2)


if __name__ == "__main__":
    main()