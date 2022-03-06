"""
Tehtävä 17.1
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

from pankkitili import Pankkitili

def main():
    p1  = Pankkitili(500, 'Pekka Python')
    p1.print_meta()


if __name__ == "__main__":
    main()