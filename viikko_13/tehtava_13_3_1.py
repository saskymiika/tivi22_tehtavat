"""
Tehtävä 13.3.1
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""


def main():
    T = (23, 45, 93, 59, 35, 58, 19, 3)
    try:
        luku = int(input("Syötä kokonaisluku: ").strip())
        if luku in T:
            print(f'Syöttämäsi luku {luku} sisältyy tuplen T{T} joukkoon.')
        else:
            print(f'Syöttämäsi luku {luku} ei sisälly tuplen T{T} joukkoon.')

    except ValueError as e:
        print('{}'.format(e))


if __name__ == "__main__":
    main()