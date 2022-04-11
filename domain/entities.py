import unittest
class Carte:
    
    
    def __init__(self, id, titlu, autor, descriere):
        self.__id = id
        self.__titlu = titlu
        self.__autor = autor
        self.__descriere = descriere

    def get_id(self):
        return self.__id


    def get_titlu(self):
        return self.__titlu


    def get_autor(self):
        return self.__autor


    def get_descriere(self):
        return self.__descriere


    def set_titlu(self, value):
        self.__titlu = value


    def set_autor(self, value):
        self.__autor = value


    def set_descriere(self, value):
        self.__descriere = value

    def __str__(self):
        return str(self.__id)+" "+self.__titlu+" "+self.__autor+" "+self.__descriere
    
    def __eq__(self,other):
        
        return self.__id== other.__id
        
    


class TestCaseCarte(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    def testInitCarte(self):
        
        
        testCarte = Carte(1, "1984", "orwell","clasice")
        
        self.assertEqual(Carte.get_id(testCarte), 1, "INITIALIZARE CARTE. ID")
        self.assertEqual(Carte.get_titlu(testCarte), "1984", "INITIALIZARE CARTE TITLU")
        self.assertEqual(Carte.get_autor(testCarte), "orwell", "INITIALIZARE CARTE AUTOR")
        self.assertEqual(Carte.get_descriere(testCarte), "clasice", "INITIALIZARE CARTE DESCRIERE")
    
    def testSetTitlu(self):
       
        testCarte = Carte(1, "1984", "orwell","clasice")
        
        Carte.set_titlu(testCarte,"ferma animalelor")
        newTestCarte = Carte(1, "ferma animalelor", "orwell","clasice")
        
        self.assertEqual(Carte.get_id(testCarte), Carte.get_id(newTestCarte), "SET ID")
        self.assertEqual(Carte.get_titlu(testCarte), Carte.get_titlu(newTestCarte), "SET TITLU")
        self.assertEqual(Carte.get_autor(testCarte), Carte.get_autor(newTestCarte), "SET AUTOR")
        self.assertEqual(Carte.get_descriere(testCarte), Carte.get_descriere(newTestCarte), "SET DESCRIERE")
    
    def testSetAutor(self):
        
        
        testCarte = Carte(1, "1984", "orwell","clasice")
        Carte.set_autor(testCarte, "george orwell")
        newTestCarte = Carte(1, "1984", "george orwell","clasice")
        
        self.assertEqual(Carte.get_id(testCarte),Carte.get_id(newTestCarte), "SET ID")
        self.assertEqual(Carte.get_titlu(testCarte), Carte.get_titlu(newTestCarte), "SET TITLU")
        self.assertEqual(Carte.get_autor(testCarte), Carte.get_autor(newTestCarte), "SET. AUTOR")
        self.assertEqual(Carte.get_descriere(testCarte), Carte.get_descriere(newTestCarte), "SET DESCRIERE")
        
    def testSetDescriere(self):
        
        testCarte=Carte(1, "1984", "orwell","clasice")
        Carte.set_descriere(testCarte, "literartura universala")
        newTestCarte=Carte(1, "1984", "orwell","literartura universala")
        
        self.assertEqual(Carte.get_id(testCarte),Carte.get_id(newTestCarte), "SET ID")
        self.assertEqual(Carte.get_titlu(testCarte), Carte.get_titlu(newTestCarte), "SET TITLU")
        self.assertEqual(Carte.get_autor(testCarte), Carte.get_autor(newTestCarte), "SET. AUTOR")
        self.assertEqual(Carte.get_descriere(testCarte), Carte.get_descriere(newTestCarte), "SET DESCRIERE")
        
  
#unittest.main()
      



class Persoana:

    
    def __init__(self, id1,nume,cnp):
        self.__id1 = id1
        self.__nume = nume
        self.__cnp = cnp

    def get_id1(self):
        return self.__id1


    def get_nume(self):
        return self.__nume
    
    def get_cnp(self):
        return self.__cnp

    def set_nume(self, value):
        self.__nume = value
    
    def set_cnp(self,value):
        self.__cnp=value

    def __str__(self):
        return str(self.__id1)+" "+self.__nume+" "+str(self.__cnp)
    
    def __eq__(self,other):
        return self.__id1== other.__id1
        

class TestCasePersoana(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testInitPersoana(self):
        
        
        testPersoana = Persoana(1, "Vlad", 3)
        
        self.assertEqual(Persoana.get_id1(testPersoana), 1, "INITIALIZARE PERSOANA ID")
        self.assertEqual(Persoana.get_nume(testPersoana), "Vlad", "INITIALIZARE PERSOANA NUME")
        self.assertEqual(Persoana.get_cnp(testPersoana), 3, "INITIALIZARE PERSOANA CNP")
        
    
    def testSetNume(self):
       
        testPersoana = Persoana(1, "Vlad", 3)
        
        Persoana.set_nume(testPersoana, "Matei")
        newTestPersoana =Persoana(1, "Matei", 3)
        
        self.assertEqual(Persoana.get_id1(testPersoana), Persoana.get_id1(newTestPersoana), "SET ID")
        self.assertEqual(Persoana.get_nume(testPersoana), Persoana.get_nume(newTestPersoana), "SET NUME")
        self.assertEqual(Persoana.get_cnp(testPersoana), Persoana.get_cnp(newTestPersoana), "SET CNP")
        
    
    def testSetCnp(self):
        
        testPersoana = Persoana(1, "Vlad", 3)
        
        Persoana.set_cnp(testPersoana, 4)
        newTestPersoana =Persoana(1, "Vlad", 4)
        
        self.assertEqual(Persoana.get_id1(testPersoana), Persoana.get_id1(newTestPersoana), "SET ID")
        self.assertEqual(Persoana.get_nume(testPersoana), Persoana.get_nume(newTestPersoana), "SET NUME")
        self.assertEqual(Persoana.get_cnp(testPersoana), Persoana.get_cnp(newTestPersoana), "SET CNP")
        
    
    #unittest.main()
#if  __name__ == "__main__":
 #   unittest.main()    
    
class Inchiriere:
    
    def __init__(self,id_i,carte,client):
        self.__id_i = id_i
        self.__carte = carte
        self.__client = client
        

    def get_id_i(self):
        return self.__id_i


    def get_carte(self):
        return self.__carte


    def get_client(self):
        return self.__client

    def __eq__(self,other):  
        return self.__id_i==other.__id_i
    
    def __str__(self):
        pass
   
class TestCaseInchiriere(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    def testInitInchiriere(self):
        
        carte=Carte(12,"Odisea","Homer","clasice")
        persoana=Persoana(15,"Andrei",6)
        id_i=1
        inchiriere=Inchiriere(id_i,carte,persoana)
        
        self.assertEqual(inchiriere.get_id_i(),1 , "")
        self.assertEqual(inchiriere.get_carte(),carte , "")
        self.assertEqual(inchiriere.get_client(),persoana , "")
        
    


class InchiriereDTO:
    
    
    def __init__(self, id_inchiriere, carte, client):
        self.__id_inchiriere = id_inchiriere
        self.__carte = carte
        self.__client = client
       

    def __str__(self):
       return str(self.__id_inchiriere)+" "+self.__carte.get_titlu()+" a fost inchiriata de "+self.__client.get_nume()
       #return str(self.__id_inchiriere)+" "+str(self.__carte)+" a fost inchiriata de "+str(self.__client)
       
   
    
if  __name__ == "__main__":
    unittest.main() 



