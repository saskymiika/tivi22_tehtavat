"""
Tehtävä 12.4
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

def main():
    data = [["Susanna Joki", 57394, "susjok@esimerkki.com"], ["Jukka Mäki", 48539, "jukmak@esimerkki.com"], 
    ["Simo Holm", 58302, "simhol@esimerkki.com"], ["Heikki Ukkonen", 48502, "heiukk@esimerkki.com"], 
    ["Topi Lukko", 48291, "topluk@esimerkki.com", "Taina Elo", 58201, "taielo@esimerkki.com"], ["Jane Eno", 48293, "janeno@esimerkki.com"], 
    ["Joona Peso", 23945, "joopes@esimerkki.com"], ["Antton Mäki", 85823, "antmak@esimerkki.com"]]

    print(f'\n{"NIMI": <16}'+' |   ID    | '+f'SÄHKÖPOSTI'.rjust(14))
    print('-------------------------------------------------')
    for p in data:
        print(f'{p[0].ljust(16)} |  {p[1]}  | {p[2].rjust(22)}')


if __name__ == "__main__":
    main()