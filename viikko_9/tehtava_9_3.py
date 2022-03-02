"""
Tehtävä 9.3
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

import io, os

def main():

    filedir = os.path.dirname(__file__)+'\\rainbow.txt'

    # avaa tiedosto cities.txt ja vie muuttujaan kaupungit
    with io.open(filedir, "r", encoding="utf-8") as f:
        rainbow = f.read().strip().split('\n')
        # while silmukkalla..?
        i = 0
        while i < len(rainbow):
            print(rainbow[i].upper())
            i += 1

        f.close()


if __name__ == "__main__":
    main()