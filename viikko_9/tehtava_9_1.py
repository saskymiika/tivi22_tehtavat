"""
Tehtävä 9.1
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

import io, os

def main():

    tiedostopolku = os.path.dirname(__file__)+'\\cities.txt'

    # avaa tiedosto cities.txt ja vie muuttujaan kaupungit
    kaupungit = io.open(tiedostopolku, "r", encoding="utf-8").read()
    print(kaupungit)


if __name__ == "__main__":
    main()