# Auto-luokkien määritykset

class Auto():
    # Olionmuodostin eli konstruktori yliluokalle Auto
    def __init__(self, rek, merkki, malli, vm, km, kvoima, vaihteisto, vari, paastot):
        """Auto-luokka malline auto-olioille yliluokka eri autotyypeille

        Args:
            rek (string): Auton rekisterinumero esim. CPM-186
            merkki (string): Auton valmistaja
            malli (string): Tyyppimerkintä
            vm (integer): Vuosimalli
            km (integer): Ajetut kilometrit
            kvoima (string): Käyttövoima; diesel, bensiini, hybridi, sähkö, kaasu, vety
            vaihteisto (string): Vaihteiston tyyppi; käsi, automaatti
            vari (string): Auton pääväri
            paastot (integer): Hiilidioksidipäästö g/km
        """
        self.rek = rek
        self.merkki = merkki
        self.malli = malli
        self.vm = vm
        self.km = km
        self.kvoima = kvoima
        self.vaihteisto = vaihteisto
        self.vari = vari
        self.paastot = paastot

    # Henkilöauton aliluokka, yliluokkana Auto, perii kaikki Auto-luokan ominaisuudet
class Henkiloauto(Auto):
        # Henkiloauto-objektien konstruktori
    def __init__(self,  rek, merkki, malli, vm, km, kvoima, vaihteisto, vari, paastot, istuimet, ovet, korimalli, tavaratila, lisavarusteet):
        super().__init__(rek, merkki, malli, vm, km, kvoima, vaihteisto, vari, paastot)
        """Henkilöaoutoluokka, yliluokkana Auto-luokka

        Args:
            istuimet (integer): Penkkien määrä
            ovet (integer): Ovien määrä
            korimalli (string): Mallit; porrasperä, viistoperä, farmari, tila-auto
            tavaratila (integer): Tavaratilan tilavuus litroina
            lisavarusteet (list): Lista lisävarusteista
        """
        self.istuimet = istuimet
        self.ovet = ovet
        self.korimalli = korimalli
        self.tavaratila = tavaratila
        self.lisavarusteet = lisavarusteet

if __name__ == "__main__":
    henkiloauto1 = Henkiloauto('CYF-67','Land-Rover','Discovery 3 HS',2008, 368210, 'diesel', 'automaatti', 'vihreä', 270, 7, 5, 'tila-auto', 300,['vakionopeuden säädin', 'peruutuskamera'])
    print('Rekisterinumero:', henkiloauto1.rek, 'istumapaikkoja:', henkiloauto1.istuimet)

# TODO: Lasketaan jäljelläolevien kilometrien hinta 