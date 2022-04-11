from errors.exceptions import ValidationException
from domain.entities import Carte,Persoana,Inchiriere
import unittest

class ValidatorCarte:
    
    def valideaza_c(self,carte):
        '''
         Functia verifica daca cartea introdusa are id,titulu,autor,descriere valida
         Daca cel putin una dintre conditii nu este indeplinita se arunca 
         ValidationError cu mesajul corepunzator
         
         ''' 
        errors =""
        if carte.get_id()<0:
            errors += "id invalid!\n"
        if carte.get_titlu()=="":
            errors += "titlu invalid!\n"
        if carte.get_autor()=="":
            errors +="autor invalid!\n"
        if carte.get_descriere()=="":
            errors +="descriere invalida!\n"
        if len(errors)>0:
            raise ValidationException(errors)
        
class TestCaseValidCarte(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testValid(self):
        
        validator_carti=ValidatorCarte()
        carte_invalida=Carte(-12,"","","")
        try:
            validator_carti.valideaza_c(carte_invalida)
            self.assertFalse(False, "CARTE INVALIDA")
        except ValidationException as ve:
            self.assertEqual(str(ve),"id invalid!\ntitlu invalid!\nautor invalid!\ndescriere invalida!\n")
        carte_invalida1=Carte(-12,"1984","orwell","clasice")
        try:
            validator_carti.valideaza_c(carte_invalida1)
            self.assertFalse(False, "CARTE INVALIDA")
        except ValidationException as ve:
            self.assertEqual(str(ve),"id invalid!\n")
        carte_invalida2=Carte(12,"","orwell","clasice")
        try:
            validator_carti.valideaza_c(carte_invalida2)
            self.assertFalse(False, "CARTE INVALIDA")
        except ValidationException as ve:
            self.assertEqual(str(ve),"titlu invalid!\n")
            
        carte_invalida3=Carte(12,"1984","","clasice")
        try:
            validator_carti.valideaza_c(carte_invalida3)
            self.assertFalse(False, "CARTE INVALIDA")
        except ValidationException as ve:
            self.assertEqual(str(ve),"autor invalid!\n")
            
        carte_invalida4=Carte(12,"1984","orwell","")
        try:
            validator_carti.valideaza_c(carte_invalida4)
            self.assertFalse(False, "CARTE INVALIDA")
        except ValidationException as ve:
            self.assertEqual(str(ve),"descriere invalida!\n")
        carte_valida=Carte(12,"Poezii","Bacovia","literatura romana")
        validator_carti.valideaza_c(carte_valida)
        self.assertTrue(True, "CARTE VALIDA")
        
    
class ValidatorPersoana:
    
    def valideaza_p(self,persoana):
        errors1=""
        if persoana.get_id1()<0:
            errors1 += "id1 invalid!\n"
        if persoana.get_nume()=="":
            errors1 += "nume invalid!\n" 
        if persoana.get_cnp()>10 or persoana.get_cnp()<0:
            errors1 += "cnp invalid!\n"
        if len(errors1)>0:
            raise ValidationException(errors1)


class TestCaseValidPers(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testValid(self):
        
        validator_pers=ValidatorPersoana()
        persoana=Persoana(-15,"",11)
        try:
            validator_pers.valideaza_p(persoana)
            self.assertFalse(False, "CLIENT INVALID")
        except ValidationException as ve:
            self.assertEqual(str(ve),"id1 invalid!\nnume invalid!\ncnp invalid!\n", "")
        persoana_valida=Persoana(14,"Radu",4)
        validator_pers.valideaza_p(persoana_valida)
        self.assertTrue(True, "CLIENT VALID")
        persoana1=Persoana(-15,"matei",6)
        try:
            validator_pers.valideaza_p(persoana1)
            self.assertFalse(False, "CLIENT INVALID")
        except ValidationException as ve:
            self.assertEqual(str(ve),"id1 invalid!\n")
        persoana3=Persoana(15,"",7)
        try:
            validator_pers.valideaza_p(persoana3)
            self.assertFalse(False, "CLIENT INVALID")
        except ValidationException as ve:
            self.assertEqual(str(ve),"nume invalid!\n")
        persoana4=Persoana(15,"matei",11)
        try:
            validator_pers.valideaza_p(persoana4)
            self.assertFalse(False, "CLIENT INVALID")
        except ValidationException as ve:
            self.assertEqual(str(ve),"cnp invalid!\n")
        
        
     

class ValidatorInchiriere:
    
    def valideaza_i(self,inchiriere):
        errors2=""
        if inchiriere.get_id_i()<0:
           errors2 += "id_i invalid!\n"
        if len(errors2)>0:
            raise ValidationException(errors2)

class TestCaseValidInch(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testValid(self):
        
        inchiriere=Inchiriere(-15,2,3)
        validator_inchirieri=ValidatorInchiriere()
        try:
            validator_inchirieri.valideaza_i(inchiriere)
            self.assertFalse(False, "INCH INVALIDA")
        except ValidationException as te:
            self.assertEqual(str(te),"id_i invalid!\n","")
        inchiriere_valida=Inchiriere(14,5,4)
        validator_inchirieri.valideaza_i(inchiriere_valida)
        self.assertTrue(True, "INCH VALIDA")




if  __name__ == "__main__":
    unittest.main() 

