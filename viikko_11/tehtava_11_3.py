"""
Tehtävä 11.3
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

from datetime import datetime


def main():
    today = datetime.today()
    vappu = datetime(2022, 5, 1)
    joulu = datetime(2022, 12, 24)

    print('\nJouluun', (joulu - today).days, 'päivää ja vappuun', (vappu - today).days, 'päivää.')

    tps = (datetime(2022, 12, 21) - today).days
    kps = (datetime(2022, 6, 21) - today).days

    if tps >= kps:
        print('\nKesäpäivänseisaus on lähempänä kuin talvipäivänseisaus.')
    else:
        print('\nTalvipäivänseisaus on lähempänä kuin kesäpäivänseisaus.')


if __name__ == "__main__":
    main()