"""
 In oop (object oriented programming) bestaan er 2 soorten relaties die tussen objecten/classes kunnen bestaan nl:
    1. is-een
    2. heeft-een

voorbeeld is-een: een auto is een voertuig, een fiets is een voertuig, ...
voorbeeld heeft-een, een persoon heeft een adres, een bedrijf heeft een adres, ...
"""

#   1. Is-een

class Voertuig:

    def beweeg(self):
        raise NotImplemented()

class Auto(Voertuig):

    def beweeg(self):
        print("ik rijd")

class Boot(Voertuig):

    def beweeg(self):
        print("ik vaar")

class Fiets(Voertuig):
    
    pass


#   2. Heeft-een

class Adres:

    def __init__(self, straat, nummer, postcode, plaats):
        self.straat = straat
        self.nummer = nummer
        self.postcode = postcode
        self.plaats = plaats

class Persoon:

    def __init__(self, naam, voornaam, adres):
        self.naam = naam
        self.voornaam = voornaam
        self.adres = adres

class Bedrijf:

    def __init__(self, naam, adres):
        self.naam = naam
        self.adres = adres


if __name__ == "__main__":

    auto = Auto()
    auto.beweeg()

    boot = Boot()
    boot.beweeg()

    fiets = Fiets()
    # fiets.beweeg()

    adres1 = Adres(" Merholaan",  "1B", 2981, "Zoersel-Parwijs")

    marcel = Persoon("Marcel", "Kiekeboe", adres1)

    marcelNv = Bedrijf("Marcel N.V.", adres1)

    print(marcel.adres.straat)
