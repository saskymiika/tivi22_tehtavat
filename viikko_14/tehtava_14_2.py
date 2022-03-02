"""
Tehtävä 14.2
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

import re


def USD2EUR(usd: float):
    # Kerroin: 1 USD = 0.831467 EUR (float)
    # muunnettu_arvo: Dollarit Euroina (float)
    return usd * 0.831467
    
def USD2GBP(usd: float):
    # Kerroin: 1 USD = 0.739472 GBP
    # muunnettu_arvo: Dollarit Euroina (float)
    return usd * 0.739472
    
def USD2JPY(usd: float):
    # Kerroin: 1 USD = 112.656 JPY 
    # muunnettu_arvo: Dollarit Euroina (float)
    return usd * 112.656

def main():
    usd = input("Syötä dollarit USD: $").strip()

    # Find right pattern for the dollar value
    m = re.match(r'\b\d+\.\d+|\d+', usd)

    if m != None:
        usd = float(usd[m.start():m.end()])

        # Euroiksi
        eur = round(USD2EUR(usd), 2)
        # Punniksi
        gbp = round(USD2GBP(usd), 2)
        # Jeneiksi
        jpy = round(USD2JPY(usd), 2)

        print("\n$%s USD = %s EUR, %s GBP, %s JPY" % (usd, eur, gbp, jpy))


if __name__ == "__main__":
    main()