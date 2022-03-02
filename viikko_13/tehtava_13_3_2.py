"""
Tehtävä 13.3.2
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""


def main():
    T = (23, 45, 93, 59, 35, 58, 19, 3)
    
    print(f'Tuplen T lukujen keskiarvo on: (%s + %s + %s + %s + %s + %s + %s + %s) / {len(T)} = {sum(T) / len(T)}' % T)


if __name__ == "__main__":
    main()