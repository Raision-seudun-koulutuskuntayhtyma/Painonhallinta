# Tietokantamoduli

# Modulien ja kirjastojen lataukset
import sqlite3

# Luodaan uusi tietokanta projektin hakemistoon
tietokanta = 'painonhallinta.db'

def luo_tietokanta(tiedosto):
    """Luo tietokannan huom. tiedoston tyyppi po. .db

    Args:
        tiedosto (string): SQL Lite tietokantatiedoston nimi
    """
    yhteys = sqlite3.connect(tiedosto)
    yhteys.close()

def luo_taulut():
    """Luo SQL Lite tietokantaan tarvittavat taulut
    """
    # Muodostetaan yhteys tietokantaan, luodaan kanta tarvittaessa
    yhteys = sqlite3.connect(tietokanta)

    # Luodaan Henkilö-taulu
    yhteys.execute('''CREATE TABLE henkilo
        (henkilo_id INTEGER PRIMARY KEY NOT NULL,
        etunimi TEXT NOT NULL,
        sukunimi TEXT NOT NULL,
        sukupuoli INTEGER NOT NULL,
        spaiva DATE NOT NULL);''')

    # Luodaan Mittaukset-taulu
    yhteys.execute('''CREATE TABLE mittaus 
        (mittaus_id INTEGER PRIMARY KEY NOT NULL,
        henkilo_id INTEGER NOT NULL,
        pituus REAL NOT NULL,
        paino REAL NOT NULL);''')
    
    # Suljetaan tietokantayhteys taulujen luonnin jälkeen
    yhteys.close()

# Luodaan testidataa
# TODO: luo rutiinit henkilön ja mittauksen tietojen syöttämiseen

# TODO: luo rutiini tietojen lukemiseksi molemmista tauluita

# Paikallinen tetaus
if __name__ == "__main__":
    luo_tietokanta(tietokanta)
    luo_taulut()
