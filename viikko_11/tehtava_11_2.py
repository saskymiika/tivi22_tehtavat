"""
Tehtävä 11.2
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

import re
from datetime import time, datetime

def main():

    print('AIKA (17:39:10):')
    t = time(hour=17, minute=39, second=10)
    print("1)", t.strftime("%I:%M:%S %p"))
    print("2)", t.strftime("%H:%M:%S"))
    print("3)", t.strftime("%H.%M.%S"))

    print('\nPVM (23.10.2028):')
    d = datetime(2028, 10, 23)
    print("1)", d.strftime("%b %d, %Y"))
    print("2)", d.strftime("%d/%m/%y"))
    print("3)", d.strftime("%d/%B/%Y"))
    print("4)", d.strftime("%A %B %d"))
    print("5)", d.strftime("%d.%m.%Y"))
    
    while True:
        sp = input('\nSyötä syntymäpäiväsi (pp.kk.vvvv): ')
        match = re.search(r"\b\d+\.\d+\.\d+\b", sp) 

        if match != None:
            sp = sp[match.start():match.end()].split('.')
            try:
                sp = datetime(int(sp[2]), int(sp[1]), int(sp[0]))
                vk = ['maanantai', 'tiistai', 'keskiviikko', 'torstai', 'perjantai', 'lauantai', 'sunnuntai']
                print('Kun synnyit oli', vk[int(sp.strftime("%w"))]+'.')
                break
            except Exception:
                print('Syötit viallisen päivämäärän.')
                pass

if __name__ == "__main__":
    main()