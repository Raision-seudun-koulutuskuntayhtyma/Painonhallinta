# Modulin avulla luodaan, luetaan ja kirjoitetaan CSV-tiedostoja

# Kirjastojen ja modulien lataukset
import csv

# Luodaan otsikot CSV-tiedostoon
def luo_otskot(tiedosto):
# Määritellään csv-tiedosto, erotin ja tekstitunniste    
    with open(tiedosto, mode='w') as datatiedosto:
        csv_kirjoittaja = csv.writer(datatiedosto, dialect='excel', delimiter=';', quotechar='"')
        csv_kirjoittaja.writerow(['Etunimi', 'Sukunimi', 'Pituus', 'Paino', 'Ikä', 'Sukupuoli', 'Tavoitepaino'])

# Lisätään rivejä CSV-tiedostoon
def lisaa_tiedot(tiedosto, etunimi, sukunimi, pituus, paino, ika, sukupuoli, tavoitepaino):
    with open(tiedosto, mode='a') as datatiedosto:
        csv_kirjoittaja = csv.writer(datatiedosto, dialect='excel', delimiter=';', quotechar='"')
        csv_kirjoittaja.writerow([etunimi, sukunimi, pituus, paino, ika, sukupuoli, tavoitepaino])
    



if __name__ == "__main__":

    # Lisätään testimielessä rivejä
    lisaa_tiedot('bmidata.csv', 'Mika', 'Vainio', '171', '72', '59','1', '70')
    lisaa_tiedot('bmidata.csv', 'Mikko', 'Viljanen', '176', '80', '50','1', '75')

    # Luetaan tiedot
    with open('bmidata.csv', 'r') as testiluku:
        print(testiluku.read())