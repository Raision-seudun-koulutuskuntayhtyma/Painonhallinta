# Tietokantamoduli

# Modulien ja kirjastojen lataukset
import sqlite3
from sqlite3.dbapi2 import SQLITE_INSERT

# Luodaan uusi tietokanta projektin hakemistoon
tietokannan_nimi = 'painonhallinta.db'

def luo_tietokanta(tiedosto):
    """Luo tietokannan huom. tiedoston tyyppi po. .db

    Args:
        tiedosto (string): SQL Lite tietokantatiedoston nimi
    """
    yhteys = sqlite3.connect(tiedosto)
    yhteys.close()

def luo_taulut(tiedosto):
    """Luo SQL Lite tietokantaan tarvittavat taulut
    """
    # Muodostetaan yhteys tietokantaan, luodaan kanta tarvittaessa
    yhteys = sqlite3.connect(tiedosto)

    # Luodaan Henkilö-taulu
    yhteys.execute('''CREATE TABLE henkilo
        (henkilo_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
        etunimi TEXT NOT NULL,
        sukunimi TEXT NOT NULL,
        sukupuoli INTEGER NOT NULL,
        spaiva DATE NOT NULL);''')

    # Luodaan Mittaukset-taulu
    yhteys.execute('''CREATE TABLE mittaus 
        (mittaus_id INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
        henkilo_id INTEGER NOT NULL,
        pituus REAL NOT NULL,
        paino REAL NOT NULL,
        FOREIGN KEY (henkilo_id)
            REFERENCES henkilo (henkilo_id)
            ON DELETE CASCADE);''')
            
    
    # Suljetaan tietokantayhteys taulujen luonnin jälkeen
    yhteys.close()

# Luodaan testidataa
def lisaa_henkilo(tiedosto, etunimi, sukunimi, spaiva, sukupuoli):
    yhteys = sqlite3.connect(tiedosto)

    yhteys.execute(" INSERT INTO henkilo (etunimi, sukunimi, spaiva, sukupuoli) VALUES ( etunimi, sukunimi)")

    

# TODO: luo rutiini tietojen lukemiseksi molemmista tauluita

# Paikallinen tetaus
if __name__ == "__main__":
    luo_tietokanta(tietokannan_nimi)
    luo_taulut(tietokannan_nimi)
