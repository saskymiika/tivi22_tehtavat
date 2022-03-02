"""
Tehtävä 14.1
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

import sys, io, os


def main():
    args = []
    for a in (sys.argv):
        if a.isdigit():
            args.append(int(a))

    args.sort()
    print('\nLuvut järjestettynä ovat:', ' '.join(map(str, args)))

    file_path = os.path.dirname(__file__) + '\\jarjestetyt_luvut.txt'

    with io.open(file_path, 'w', encoding='utf-8') as f:
        f.write(' '.join(map(str, args)))
        f.close()

    print('\nKiitos ohjelman käytöstä.')


if __name__ == "__main__":
    main()