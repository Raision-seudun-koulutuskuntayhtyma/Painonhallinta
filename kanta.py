# Tietokantamoduli

# Modulien ja kirjastojen lataukset
import sqlite3

# Luodaan uusi tietokanta projektin hakemistoon
yhteys = sqlite3.connect('painohallinta.db')

# Luodaan Henkilö-taulu
yhteys.execute('''CREATE TABLE henkilo (henkilo_id INTEGER PRIMARY KEY NOT NULL, etunimi TEXT NOT NULL, sukunimi TEXT NOT NULL, sukupuoli INTEGER NOT NULL, spaiva DATE NOT NULL)''')

# Luodaan testidataa
