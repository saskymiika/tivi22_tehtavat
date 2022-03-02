"""
Tehtävä 14.2.1
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""


NUMEROT = [1, 2, 3, 4, 5, 6]

def kaanna():
    global NUMEROT
    NUMEROT = NUMEROT[::-1]

def main():

    print("Ennen kääntöä, NUMEROT =", NUMEROT)
    # listan kääntö
    kaanna()
    print("Käännön jälkeen, NUMEROT =", NUMEROT)    


if __name__ == "__main__":
    main()
