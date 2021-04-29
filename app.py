# Konsolisovelluksen lopullinen pääohjelma

# Modulien ja kirjastojen lataukset
import kanta # Tietokannan käsittelyssä tarvittavat komponentit
import kysymys # Tietojen syöttämiseen liittyvät kysymisrutiinit
import luokat # Henkilö, Aikuinen ja Lapsi -luokkien määrittelyt

# Varsinainen ohjema
while True:
    
    # Silmukka henkilötietojen kyselemiseen
    lisaa_henkiloita = input('Lisätäänkö uusia henkilöitä? K/e')
    if lisaa_henkiloita.upper() != 'E':
        lisaa_henkiloita = 'K'

    while lisaa_henkiloita.upper() == 'K':
        etunimi = input('etunimi: ')
        sukunimi = input('sukunimi: ')
        sukupuoli = kysymys.kysy_liukuluku('Sukupuoli nainen 0, mies 1: ', 0, 1)
        syntyma_aika = input('Syntymäaika (VVVV-KK-PP): ') 
        lisaa_henkiloita = input('Lisätäänkö uusia henkilöitä? K/e')
        if lisaa_henkiloita.upper() == 'E':
            break
        else:
            lisaa_henkiloita = 'K'

    # Silmukka mittaustietojen kyselemiseen
    lisaa_mittauksia = input('Lisätäänkö uusia mittaustuloksia? k/E')
    while lisaa_mittauksia.upper() == 'K':
        pituus = kysymys.kysy_liukuluku('Pituus (cm): ', 100, 250)
        paino = kysymys.kysy_liukuluku('Paino (kg): ', 30, 200)
    