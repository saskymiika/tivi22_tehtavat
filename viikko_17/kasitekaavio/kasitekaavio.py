from datetime import datetime

class Kurssi:
    def __init__(self, kurssikoodi: int, nimi: str, ov: int, kuvaus: str):
        self.kurssikoodi = kurssikoodi
        self.nimi = nimi
        self.ov = ov
        self.kuvaus = kuvaus


class Opiskelija: 
    def __init__(self, opiskelijanumero: int, nimi: str, osoite: str, puhelinnumero: str, syntyma_aika: datetime):
        self.opiskelijanumero = opiskelijanumero
        self.nimi = nimi
        self.osoite = osoite
        self.puhelinnumero = puhelinnumero
        self.syntyma_aika = syntyma_aika


class Opettaja:
    def __init__(self, nimi:str, osoite: str, puhelinnumero: str, oppiaine: str):
        self.nimi = nimi
        self.osoite = osoite
        self.puhelinnumero = puhelinnumero
        self.oppiaine = oppiaine


class Kotitehtava:
    def __init__(self, numero: int, kuvaus: str, palautus_paivamaara: datetime):
        self.numero = numero
        self.kuvaus = kuvaus
        self.palautus_paivamaara = palautus_paivamaara