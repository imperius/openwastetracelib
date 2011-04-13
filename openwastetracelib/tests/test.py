from openwastetracelib.objects import Azienda
import unittest
import random

class TestAzienda(unittest.TestCase):
    """ Base test for Azienda object. """

    def setUp(self):
        """ Create basic Azienda object """
        ragioneSociale = "Ragione Sociale S.r.l."
#        codiceFiscale = "1234567890"
        codiceFiscale = str(random.random()).split(".")[1]
#        versione = 1
        versione = random.randint(1,9)
#        idSIS = "12345"
        idSIS = str(random.random()).split(".")[1]
        self.azienda = Azienda(ragioneSociale,codiceFiscale,versione,idSIS)

    def test_extra_attribute(self):
        """ Test adding of attribute pIVA"""
#        self.azienda.pIva = "0987654321"
        self.azienda.pIva = str(random.random()).split(".")[1]

if __name__ == '__main__':
    unittest.main()
