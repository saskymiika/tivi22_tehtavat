"""
Tehtävä 14.4
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

from html.entities import html5
import re, pydoc


def USD2EUR(usd: float):
    # Kerroin: 1 USD = 0.831467 EUR (float)
    # muunnettu_arvo: Dollarit Euroina (float)
    return round(usd * 0.831467, )
    
def USD2GBP(usd: float):
    # Kerroin: 1 USD = 0.739472 GBP
    # muunnettu_arvo: Dollarit Euroina (float)
    return round(usd * 0.739472, 2)
    
def USD2JPY(usd: float):
    # Kerroin: 1 USD = 112.656 JPY 
    # muunnettu_arvo: Dollarit Euroina (float)
    return round(usd * 112.656, 2)

def EUR2GBP(eur: float):
    # Kerroin: 1 USD = 0.889358 GBP 
    # muunnettu_arvo: Dollarit Euroina (float)
    return round(eur * 0.889358, 2)

def main():
    usd = input("Syötä dollarit USD: $").strip()

    # Find right pattern for the dollar value
    m = re.match(r'\b\d+\.\d+|\d+', usd)

    if m != None:
        usd = float(usd[m.start():m.end()])
        # Euroiksi
        eur = USD2EUR(usd)
        # Punniksi
        gbp = USD2GBP(usd)
        # Jeneiksi
        jpy = USD2JPY(usd)

        print("\n$%s USD = %s EUR, %s GBP, %s JPY" % (usd, eur, gbp, jpy))

        pydoc.writedoc("tehtava_14_4")

        # voisimme suorittaa saman komentoriviltä suoraan:
        # python -m pydoc -w <path-to-file>



if __name__ == "__main__":
    main()