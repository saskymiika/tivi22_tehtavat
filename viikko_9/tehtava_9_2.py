"""
Tehtävä 9.2
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

import io, os

def main():

    tiedostopolku = os.path.dirname(__file__)+'\\cities.txt'

    # avaa tiedosto cities.txt ja vie muuttujaan kaupungit
    with io.open(tiedostopolku, "r", encoding="utf-8") as f:
        kaupungit = f.read().strip().split('\n')
        print(kaupungit)
        f.close()
        if f.closed:
            print("Striimi on suljettu.")
        else:
            print("Tiedoston lukeminen on vielä kesken.")


if __name__ == "__main__":
    main()