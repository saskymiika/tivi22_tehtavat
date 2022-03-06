"""
Tehtävä 17.4
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

from auto import Auto


def main():
    auto1 = Auto("Mersu", 195)
    auto2 = Auto("Lada", 110)
    auto3 = Auto("Lexus RRV-514", 280)
    auto4 = Auto("Trabant", 85)

    autot = [auto1, auto2, auto3, auto4]
    autot.sort(key=lambda auto: auto.huippunopeus, reverse=True)

    nopein_auto = autot[0]

    print(nopein_auto.__str__())



if __name__ == "__main__":
    main()
