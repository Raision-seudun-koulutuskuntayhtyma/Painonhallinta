# Modulin laskenta.py testit

# Modulien ja kirjastojen lataukset
import laskenta

# Ensimmäinen testi lasketaan painoindeksi ja verrataan tulosta ennalta laskettuun arvoon
def test_painoideksi():
    assert laskenta.bmi(74, 1.71) == 25.3069320474676
    