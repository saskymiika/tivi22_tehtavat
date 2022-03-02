"""
Viikko 15 Porjektitehtävä
Miika Toivanen
miika.toivanen@edu.sasky.fi


TEHTÄVÄNANTO:

NASA ylläpitää verkkosivustollaan palvelua, jossa on päivittäin vaihtuva astronominen kuva (https://apod.nasa.gov/apod).
Tässä projektissa ohjelmoit ohjelman, jolla käyttäjä lataa halutun päivämäärän mukaisen astronomisen kuvan NASAn palvelimelta paikalliselle koneelleen. 


Ohjelma tallentaa kuvan paikalliselle kiintolevylle seuraavankaltaiseen hakemistorakenteeseen ja tiedostonimeen:
---> yyyy/mm/yyyy-mm-dd.jpg. 


Valikko:
- Lataa tämän tai eilisen päivän astronominen kuva
- Lataa satunnainen kuva väliltä 16.6.1995 - <tämä_päivä>


Jokaisen kuvan binaaridata löytyy seuraavan kaltaisesta osoitteesta:
url: https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=YYYY-MM-DD

"""

from random import randint
import re, io, os
from datetime import datetime, timedelta
import requests
import PIL.Image as Image
import shutil


def valikko():
    option = input("""
Mitä haluat tehdä?

1) Ladata tämän päivän astronomisen kuvan.
2) Ladata eilisen päivän astronomisen kuvan.
3) Ladata satunnaisen astronomisen kuvan väliltä: 16.6.1995 - %s.
0) Lopeta ohjelma.

Syötä toiminto: """ % datetime.today().strftime("%d.%m.%Y"))

    if option.isdigit():
        return int(option)
    else:
        return None


def hae_kuvaa(date: datetime):
    """Hae kuvaa NASA:n palvelimalta syötetyn päivämäärän mukaan."""
    date_string = date.strftime("%Y-%m-%d")
    api_key = "LvJyfFad4ANlt6Oi7P1XAoSICxd0wdi2eSbgBfnf"
    request_url = "https://api.nasa.gov/planetary/apod"
    filename = date.strftime("%Y/%m/%d-%H-%M")+'.jpg'
    image_path = os.path.dirname(__file__) + '\\nasapics'
    metadata_path = os.path.dirname(__file__) + '\\metadata'

    pay_load = {"api_key": api_key, "date": date_string}
    with requests.get(request_url, params=pay_load) as res:
        if res.status_code == 200:
            data = res.content.decode('UTF-8')
            # or res.text decodes as default
            # data is type str so convert to DICT with eval
            data = eval(data)
            high_image_url = data.get('hdurl')
            low_image_url = data.get('url')
        res.close()
    
    # kaytetään pienempi resoluutioista kuvaa tähän
    if low_image_url != None:
        with requests.get(low_image_url, stream=True) as img:
            if img.status_code == 200:

                img.raw.decode_content = True

                with open(image_path, 'wb') as file:
                    shutil.copyfileobj(img.raw, file)
                    file.write(img.content)

                ## now we have image in bytes.



def rand_date():
    """Valitse satunnainen päivämäärä 16.6.1995 - tämän päivän väliltä."""
    df = datetime(year=1995, month=6, day=16)
    td = datetime.today()
    random_days = randint(0, (td - df).days)
    return df + timedelta(days=random_days)


def main():
    while True:
        valinta = valikko()

        if valinta != None and valinta in range(0, 4):
            if valinta == 1:
                hae_kuvaa(datetime.today())
            elif valinta == 2:
                hae_kuvaa(datetime.today() - timedelta(days=1))
            elif valinta == 3:
                print(rand_date())
            else:
                exit()
            
            



if __name__ == "__main__":
    main()