"""
Tehtävä 9.4
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

import io, os

def main():

    filedir = os.path.dirname(__file__)+'\\koirat.txt'

    with io.open(filedir, "w", encoding="utf-8") as f:
        f.write('Mäyräkoira\n')
        f.write('Lammaskoira\n')
        f.write('Noutaja\n')
        f.write('Beagle\n')
        f.close()

    with io.open(filedir, "r", encoding="utf-8") as f:
        print(f.read())
        f.close()
    
    with io.open(filedir, "a+", encoding="utf-8") as f:
        f.write('Gorgi\n')
        f.close()

    with io.open(filedir, "r", encoding="utf-8") as f:
        print(f.read().strip().split('\n'))
        f.close()



if __name__ == "__main__":
    main()