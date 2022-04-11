from errors.exceptions import RepoException
from domain.entities import Carte,Persoana,Inchiriere
import unittest



class RepositoryCarte:
    
    
    def __init__(self):
        self._elems =[] 
        
    
    def __len__(self):
        return len(self._elems)

    
    def store(self, carte):
        if carte in self._elems:
            raise RepoException("element existent!\n")
        self._elems.append(carte)
        

    def search(self, key_carte):
        """
        functia cauta obiectul de tip carte cu id=key_carte
        daca il gaseste il returneaza, daca nu arunca eroare
        """
        for elem in self._elems:
            if elem==key_carte:
               return elem
        
        raise RepoException("element inexistent!\n")
        
           
#     def search(self, key_carte,lis):
#        lis=self._elems
#        if len(lis)==0: raise RepoException("element inexistent!\n")
#        else :
#            if lis[0]==key_carte:
#                return lis[0]
#            return search(key_carte,lis[:1])
       
    
    def update(self, carte):
        #if carte not in self._elems:
         #   raise RepoException("element inexistent!\n")
        for i in range(len(self._elems)):
            if self._elems[i]==carte:
                self._elems[i]=carte
                return
        raise RepoException("element inexistent!\n")
        

    
    def remove(self, key_carte):
        if key_carte not in self._elems:
            raise RepoException("element inexistent!\n")
        for i in range(0,len(self._elems)): 
            if self._elems[i]==key_carte:
               del self._elems[i]
               return
   
    
    def get_all(self):
        return self._elems[:]
    
    def get_carte_by_id(self,carte_id):
        for carte in self._elems:
            if carte.get_id()==carte_id:
                return carte
        raise RepoException("element inexisatent ")
    

#class TestCaseCartiRepo(unittest.TestCase):

#     def setUp(self):
#         unittest.TestCase.setUp(self)
# 
#     def tearDown(self):
#         unittest.TestCase.tearDown(self)
# 
#     def testAddCarte(self):
#         repo_carti=RepositoryCarte() 
#         self.assertEqual(len(repo_carti), 0, "CARTI ADAUGATE")
#         carte=Carte(12,"Odisea","Homer","clasice")
#         repo_carti.store(carte)
#         self.assertEqual(len(repo_carti), 1, "CARTI ADAUGATE")
#         
#         self.assertEqual(Carte.get_id(repo_carti.get_all()[0]), 12, "ADAUGARE CARTE ID")
#         self.assertEqual(Carte.get_titlu(repo_carti.get_all()[0]),"Odisea","ADAUGARE TITLU CARTE")
#         self.assertEqual(Carte.get_autor(repo_carti.get_all()[0]),"Homer", "ADAUGARE CARTE AUTOR")
#         self.assertEqual(Carte.get_descriere(repo_carti.get_all()[0]), "clasice")
#         
#     
#     def testRemCarte(self):
#         
#         repo_carti=RepositoryCarte()  
#         self.assertEqual(len(repo_carti), 0, "CARTI ADAUGATE")  
#         carte=Carte(19,"Odisea","Homer","clasice") 
#         repo_carti.store(carte)
#         carte2=Carte(18,"Poezii","Bacovia","literatura romana")
#         repo_carti.store(carte2)
#         self.assertEqual(len(repo_carti), 2, "CARTI ADAUGATE")
#         key_carte=Carte(18,None,None,None)
#         repo_carti.remove(key_carte)
#         
#         self.assertEqual(Carte.get_id(repo_carti.get_all()[0]), 19, "ADAUGARE CARTE ID")
#         self.assertEqual(Carte.get_titlu(repo_carti.get_all()[0]),"Odisea","ADAUGARE TITLU CARTE")
#         self.assertEqual(Carte.get_autor(repo_carti.get_all()[0]),"Homer", "ADAUGARE CARTE AUTOR")
#         self.assertEqual(Carte.get_descriere(repo_carti.get_all()[0]), "clasice", "ADAUGARE CARTE DESCRIERE")
# #    
#     def testSearchCarte(self):
#         
#         repo_carti=RepositoryCarte()  
#         self.assertEqual(len(repo_carti), 0, "CARTI ADAUGATE")  
#         carte=Carte(19,"Odisea","Homer","clasice") 
#         repo_carti.store(carte)
#         
#         key_carte=Carte(19,None,None,None)
#         result_carte=repo_carti.search(key_carte)
#         
#         self.assertEqual(carte.get_titlu(),result_carte.get_titlu() , "CAUTARE CARTE")
#         self.assertEqual(carte.get_autor(), result_carte.get_autor(), "CAUTARE CARTE")
#         self.assertEqual(carte.get_descriere(), result_carte.get_descriere(), "CAUTARE CARTE")
        
        
            
    
class FileRepositoryCarte(RepositoryCarte):
     
     
    def __init__(self,filename):
        self.__filename=filename
        RepositoryCarte.__init__(self)
         
 
    def __citeste_tot_din_fisier(self):
        with open(self.__filename,"r") as f:
            self._elems=[]
            lines=f.readlines()
            for line in lines:
                line=line.strip()
                if line!="":
                    parts=line.split(";")
                    carte=Carte(int(parts[0]),parts[1],parts[2],parts[3])
                    self._elems.append(carte)
         
             
             
     
    def __append_carte_fisier(self, carte):
        with open(self.__filename,"a") as f:
            f.write(str(carte.get_id())+';'+carte.get_titlu()+';'+carte.get_autor()+';'+carte.get_descriere()+'\n')
     
    def __scrie_tot_in_fisier(self):
        with open(self.__filename,"w") as f:
            for carte in self._elems:
                f.write(str(carte.get_id())+';'+carte.get_titlu()+';'+carte.get_autor()+';'+carte.get_descriere()+'\n')
                 
     
    def store(self, carte):
        self.__citeste_tot_din_fisier()
        RepositoryCarte.store(self, carte)
        self.__append_carte_fisier(carte)
         
     
     
    def update(self, carte):
        self.__citeste_tot_din_fisier()
        RepositoryCarte.update(self, carte)
        self.__scrie_tot_in_fisier()
         
    def remove(self, key_carte):
        self.__citeste_tot_din_fisier()
        RepositoryCarte.remove(self, key_carte)
        self.__scrie_tot_in_fisier()
 
    def get_all(self):
        self.__citeste_tot_din_fisier()
        return RepositoryCarte.get_all(self)
     
    def __len__(self):
        self.__citeste_tot_din_fisier()
        return RepositoryCarte.__len__(self)
 
    def search(self, key_carte):
        self.__citeste_tot_din_fisier()
         
        return RepositoryCarte.search(self, key_carte)
     
    def get_carte_by_id(self, carte_id):
        self.__citeste_tot_din_fisier()
        return RepositoryCarte.get_carte_by_id(self, carte_id)
    
    
class NouFileRepositoryCarte:
    
    def __init__(self,filename):
        self.__filename=filename
        
    

    def store(self, carte):
        
        f=open(self.__filename,"a")
        f.write(str(carte.get_id()))
        f.write(";")
        f.write(carte.get_titlu())
        f.write(";")
        f.write(carte.get_autor())
        f.write(";")
        f.write(carte.get_descriere())
        f.write("\n")
        f.close()

    def get_all(self):
        f=open(self.__filename,"r")
        elems=[]
        
        for l in f:
            linie=l.strip()
            if l.strip()!=" ":
                linie=l.strip()
                parts=linie.split(";")
                carte=Carte(int(parts[0]),parts[1],parts[2],parts[3])
                elems.append(carte)
        f.close()
        return elems
        
        
    def remove(self,key):
        
        gasit=0
        
        f=open(self.__filename,'r')
        line=f.readline()
        while line:
            
            if line=="":
                line=f.readline()
            else:
                parts=line.split(";")
                carte=Carte(int(parts[0]),parts[1],parts[2],parts[3])
                x=carte.get_id()
                y=key.get_id()
                if x==y:
                    
                    gasit = 1
                    line=f.readline()
                else:
                    faux=open("auxiliar.txt","a")
                    faux.write(str(carte.get_id()))
                    faux.write(";")
                    faux.write(carte.get_titlu())
                    faux.write(";")
                    faux.write(carte.get_autor())
                    faux.write(";")
                    faux.write(carte.get_descriere())
                    
                    faux.close()
                    line=f.readline()
        f.close()
        if gasit==0:
            raise RepoException("element inexistent")
            
        with open("altt1.txt","w") as f:
            f.write("")
        faux=open("auxiliar.txt","r")
        line=faux.readline()
        while line:
            f=open(self.__filename,"a")
            f.write(line)
            f.close()
            line=faux.readline()
        faux.close()
            
            
    def update(self,carte):
        gasit=0
        
        f=open(self.__filename,'r')
        line=f.readline()
        while line:
            
            if line=="":
                line=f.readline()
            else:
                parts=line.split(";")
                carte1=Carte(int(parts[0]),parts[1],parts[2],parts[3])
                x=carte1.get_id()
                y=carte.get_id()
                if x==y:
                    
                    gasit = 1
                    faux=open("auxiliar1.txt","a")
                    faux.write(str(carte.get_id()))
                    faux.write(";")
                    faux.write(carte.get_titlu())
                    faux.write(";")
                    faux.write(carte.get_autor())
                    faux.write(";")
                    faux.write(carte.get_descriere())
                    faux.close()
                    line=f.readline()
                else:
                    faux=open("auxiliar1.txt","a")
                    faux.write(str(carte1.get_id()))
                    faux.write(";")
                    faux.write(carte1.get_titlu())
                    faux.write(";")
                    faux.write(carte1.get_autor())
                    faux.write(";")
                    faux.write(carte1.get_descriere())
                    
                    faux.close()
                    line=f.readline()
        f.close()
        if gasit==0:
            raise RepoException("element inexistent")
            
        with open("altt1.txt","w") as f:
            f.write("")
        faux=open("auxiliar1.txt","r")
        line=faux.readline()
        while line:
            f=open(self.__filename,"a")
            f.write(line)
            f.close()
            line=faux.readline()
        faux.close()
        
    def search(self,key):
        
        
        f=open(self.__filename,'r')
        line=f.readline()
        while line:
            #print(line)
            if line=="":
                line=f.readline()
            else:
                parts=line.split(";")
                carte=Carte(int(parts[0]),parts[1],parts[2],parts[3])
                x=carte.get_id()
                y=key.get_id()
                if x==y:
                    return carte
                    
                line=f.readline()
                
        raise RepoException("element inexitent")
        
    
class TestCaseCartiRepoFile(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        file = open("CARTE.txt", "r")
        file.close()
 
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        file = open("CARTE.txt", "r")
        file.close()
        
    def testAddCarte(self):
        
        
        
        with open(r"CARTE.txt","w") as f:
            f.write("")
        repo_carti=FileRepositoryCarte(r"CARTE.txt")
        
        file = open("CARTE.txt", "r")
        file.close()
        repo_carti=FileRepositoryCarte(r"CARTE.txt") 
        
        print(len(repo_carti))
        
        carte=Carte(8,"s","d","g")
        repo_carti.store(carte)
        print(len(repo_carti))
        carte=Carte(7,"s","d","g")
        repo_carti.store(carte)
        print(len(repo_carti))
        
        
       
        #self.assertEqual(len(repo_carti), 1, "CARTI ADAUGATE")
#         carte=Carte(12,"Odisea","Homer","clasice")
        
#         self.assertEqual(len(repo_carti), 2, "CARTI ADAUGATE")
        
#         carte0=Carte(12,None,None,None)
#         try:
#             repo_carti.store(carte0)
#             assert(False)
#         except RepoException as re:
#             assert(str(re)=="element existent!\n")
#              
#         self.assertEqual(Carte.get_id(repo_carti.get_all()[0]), 12, "ADAUGARE CARTE ID")
#         self.assertEqual(Carte.get_titlu(repo_carti.get_all()[0]),"Odisea","ADAUGARE TITLU CARTE")
#         self.assertEqual(Carte.get_autor(repo_carti.get_all()[0]),"Homer", "ADAUGARE CARTE AUTOR")
#         self.assertEqual(Carte.get_descriere(repo_carti.get_all()[0]), "clasice", "ADAUGARE CARTE DESCRIERE")
        
#     def testRemCarte(self):
#         
#         repo_carti=FileRepositoryCarte("cartiTeste.txt") 
#         self.assertEqual(len(repo_carti), 0, "CARTI ADAUGATE")  
#         carte=Carte(19,"Odisea","Homer","clasice") 
#         repo_carti.store(carte)
#         carte2=Carte(18,"Poezii","Bacovia","literatura romana")
#         repo_carti.store(carte2)
#         self.assertEqual(len(repo_carti), 2, "CARTI ADAUGATE")
#         key_carte=Carte(18,None,None,None)
#         repo_carti.remove(key_carte)
#         
#         self.assertEqual(Carte.get_id(repo_carti.get_all()[0]), 19, "ADAUGARE CARTE ID")
#         self.assertEqual(Carte.get_titlu(repo_carti.get_all()[0]),"Odisea","ADAUGARE TITLU CARTE")
#         self.assertEqual(Carte.get_autor(repo_carti.get_all()[0]),"Homer", "ADAUGARE CARTE AUTOR")
#         self.assertEqual(Carte.get_descriere(repo_carti.get_all()[0]), "clasice", "ADAUGARE CARTE DESCRIERE")
# #    
#     def testSearchCarte(self):
#         
#         repo_carti=FileRepositoryCarte("cartiTeste.txt")  
#         self.assertEqual(len(repo_carti), 0, "CARTI ADAUGATE")  
#         carte=Carte(19,"Odisea","Homer","clasice") 
#         repo_carti.store(carte)
#         
#         key_carte=Carte(19,None,None,None)
#         result_carte=repo_carti.search(key_carte)
#         
#         self.assertEqual(carte.get_titlu(),result_carte.get_titlu() , "CAUTARE CARTE")
#         self.assertEqual(carte.get_autor(), result_carte.get_autor(), "CAUTARE CARTE")
#         self.assertEqual(carte.get_descriere(), result_carte.get_descriere(), "CAUTARE CARTE")
#         
        
        
class RepositoryPersoana:


    def __init__(self):
        self._elems =[]

    def __len__(self):
        return len(self._elems)

    def store(self,persoana):
        if persoana in self._elems:
            raise RepoException("element existent!\n")
        self._elems.append(persoana)


    def search(self, key_persoane):
        if key_persoane not in self._elems:
            raise RepoException("element inexistent!\n")
        for elem in self._elems:
            if elem==key_persoane:
                return elem


    def update(self, persoana):
        if persoana not in self._elems:
            raise RepoException("element inexistent!\n")
        for i in range(len(self._elems)):
            if self._elems[i]==persoana:
                self._elems[i]=persoana
                return



    def remove(self, key_persoane):
        if key_persoane not in self._elems:
            raise RepoException("element inexistent!\n")
        for i in range(len(self._elems)):
            if self._elems[i]==key_persoane:
                del self._elems[i]
                return

    def get_all(self):
        return self._elems[:]

    def get_client_by_id(self,client_id):
        for client in self._elems:
            if client.get_id1()==client_id:

                return client
        raise RepoException("element inexistent! ")


# class TestCasePersRepo(unittest.TestCase):
# 
#     def setUp(self):
#         unittest.TestCase.setUp(self)
# 
#     def tearDown(self):
#         unittest.TestCase.tearDown(self)
#         
#     def testAddPers(self):
#         repo_persoane=RepositoryPersoana()
#         self.assertEqual(len(repo_persoane), 0, "CLIENTI ADAUGATI")
#         persoana=Persoana(15,"Andrei",6)
#         repo_persoane.store(persoana)
#         self.assertEqual(len(repo_persoane), 1, "CLIENTI ADAUGATI")
#         
#         self.assertEqual(Persoana.get_id1(repo_persoane.get_all()[0]), 15, "ADAUGARE CLIENT ID")
#         self.assertEqual(Persoana.get_nume(repo_persoane.get_all()[0]),"Andrei","ADAUGARE NUME CLIENT")
#         self.assertEqual(Persoana.get_cnp(repo_persoane.get_all()[0]),6, "ADAUGARE CNP CLIENT")
#         
#     def testRemPers(self):
#         repo_persoane=RepositoryPersoana()
#         self.assertEqual(len(repo_persoane), 0, "CLIENTI ADAUGATI")
#         persoana=Persoana(19,"Andrei",6)
#         repo_persoane.store(persoana)
#         self.assertEqual(len(repo_persoane), 1, "CLIENTI ADAUGATI")
#         persoana2=Persoana(15,"Cosmin",6)
#         repo_persoane.store(persoana2)
#         key_persoane=Persoana(15,None,None)
#         repo_persoane.remove(key_persoane)
#         
#         self.assertEqual(Persoana.get_id1(repo_persoane.get_all()[0]), 19, "ADAUGARE CLIENT ID")
#         self.assertEqual(Persoana.get_nume(repo_persoane.get_all()[0]),"Andrei","ADAUGARE NUME CLIENT")
#         self.assertEqual(Persoana.get_cnp(repo_persoane.get_all()[0]),6, "ADAUGARE CNP CLIENT")
#         
#         
#     def testSearchPers(self):
#         
#         repo_persoane=RepositoryPersoana()
#         self.assertEqual(len(repo_persoane), 0, "CLIENTI ADAUGATI")
#         persoana=Persoana(19,"Andrei",6)
#         repo_persoane.store(persoana)
#         
#         key_persoana=Persoana(19,None,None)
#         result_persoane=repo_persoane.search(key_persoana)
#         
#         self.assertEqual(Persoana.get_id1(repo_persoane.get_all()[0]),result_persoane.get_id1() , "ADAUGARE CLIENT ID")
#         self.assertEqual(Persoana.get_nume(repo_persoane.get_all()[0]),result_persoane.get_nume(),"ADAUGARE NUME CLIENT")
#         self.assertEqual(Persoana.get_cnp(repo_persoane.get_all()[0]),result_persoane.get_cnp(), "ADAUGARE CNP CLIENT")
#               
#   
#             
#     
class FileRepositroyPersoana(RepositoryPersoana):


    def __init__(self, filename):
        self.__filename =filename
        RepositoryPersoana.__init__(self)


    def __citeste_tot_din_fisier(self):
        with open(self.__filename,"r") as f:
            self._elems=[]
            lines=f.readlines()
            for line in lines:
                line=line.strip()
                if line!="":
                    parts=line.split(";")
                    persoana=Persoana(int(parts[0]),parts[1],int(parts[2]))
                    self._elems.append(persoana)


    def __append_persoana_fisier(self, persoana):
        with open(self.__filename,"a") as f:
            f.write(str(persoana.get_id1())+';'+persoana.get_nume()+';'+str(persoana.get_cnp())+'\n')

    def __scrie_tot_din_fisier(self):
        with open(self.__filename,"w") as f:
            for persoana in self._elems:
                f.write(str(persoana.get_id1())+';'+persoana.get_nume()+';'+str(persoana.get_cnp())+'\n')


    def store(self, persoana):
        self.__citeste_tot_din_fisier()
        RepositoryPersoana.store(self, persoana)
        self.__append_persoana_fisier(persoana)

    def get_all(self):
        self.__citeste_tot_din_fisier()
        return RepositoryPersoana.get_all(self)


    def remove(self, key_persoane):
        self.__citeste_tot_din_fisier()
        RepositoryPersoana.remove(self, key_persoane)
        self.__scrie_tot_din_fisier()

    def search(self, key_persoane):
        self.__citeste_tot_din_fisier()
        return RepositoryPersoana.search(self, key_persoane)

    def update(self, persoana):
        self.__citeste_tot_din_fisier()
        RepositoryPersoana.update(self, persoana)
        self.__scrie_tot_din_fisier()

    def __len__(self):
        self.__citeste_tot_din_fisier()
        return RepositoryPersoana.__len__(self)

    def get_client_by_id(self, client_id):
        self.__citeste_tot_din_fisier()
        return RepositoryPersoana.get_client_by_id(self, client_id)


# class TestCasePersRepoFile(unittest.TestCase):
# 
#     def setUp(self):
#         unittest.TestCase.setUp(self)
#         file = open("clientiTeste.txt", "w")
#         file.close()
#         
# 
#     def tearDown(self):
#         unittest.TestCase.tearDown(self)
#         file = open("clientiTeste.txt", "w")
#         file.close()
#         
#     def testAddPers(self):
#         repo_persoane=FileRepositroyPersoana("clientiTeste.txt")
#         self.assertEqual(len(repo_persoane), 0, "CLIENTI ADAUGATI")
#         persoana=Persoana(15,"Andrei",6)
#         repo_persoane.store(persoana)
#         self.assertEqual(len(repo_persoane), 1, "CLIENTI ADAUGATI")
#         
#         self.assertEqual(Persoana.get_id1(repo_persoane.get_all()[0]), 15, "ADAUGARE CLIENT ID")
#         self.assertEqual(Persoana.get_nume(repo_persoane.get_all()[0]),"Andrei","ADAUGARE NUME CLIENT")
#         self.assertEqual(Persoana.get_cnp(repo_persoane.get_all()[0]),6, "ADAUGARE CNP CLIENT")
#         
#     def testRemPers(self):
#         repo_persoane=FileRepositroyPersoana("clientiTeste.txt")
#         self.assertEqual(len(repo_persoane), 0, "CLIENTI ADAUGATI")
#         persoana=Persoana(19,"Andrei",6)
#         repo_persoane.store(persoana)
#         self.assertEqual(len(repo_persoane), 1, "CLIENTI ADAUGATI")
#         persoana2=Persoana(15,"Cosmin",6)
#         repo_persoane.store(persoana2)
#         key_persoane=Persoana(15,None,None)
#         repo_persoane.remove(key_persoane)
#         
#         self.assertEqual(Persoana.get_id1(repo_persoane.get_all()[0]), 19, "ADAUGARE CLIENT ID")
#         self.assertEqual(Persoana.get_nume(repo_persoane.get_all()[0]),"Andrei","ADAUGARE NUME CLIENT")
#         self.assertEqual(Persoana.get_cnp(repo_persoane.get_all()[0]),6, "ADAUGARE CNP CLIENT")
#         
#         
#     def testSearchPers(self):
#         
#         repo_persoane=FileRepositroyPersoana("clientiTeste.txt")
#         self.assertEqual(len(repo_persoane), 0, "CLIENTI ADAUGATI")
#         persoana=Persoana(19,"Andrei",6)
#         repo_persoane.store(persoana)
#         
#         key_persoana=Persoana(19,None,None)
#         result_persoane=repo_persoane.search(key_persoana)
#         
#         self.assertEqual(Persoana.get_id1(repo_persoane.get_all()[0]),result_persoane.get_id1() , "ADAUGARE CLIENT ID")
#         self.assertEqual(Persoana.get_nume(repo_persoane.get_all()[0]),result_persoane.get_nume(),"ADAUGARE NUME CLIENT")
#         self.assertEqual(Persoana.get_cnp(repo_persoane.get_all()[0]),result_persoane.get_cnp(), "ADAUGARE CNP CLIENT")
#               
#     
#   
class RepositoryInchiriere:

    def __init__(self):
        self._elems=[]

    def __len__(self):
        return len(self._elems)


    def add(self,inchiriere):
        if inchiriere in self._elems:
            raise RepoException("element existent!")
        self._elems.append(inchiriere)

    def get_all(self):
        return self._elems[:]

    def remove(self,key):
        if key not in self._elems:
            raise RepoException("element inexistenttt! ")
        for i in range(len(self._elems)):
            if self._elems[i]==key:
                del self._elems[i]
                return


# class TestCaseInchRepo(unittest.TestCase):
# 
#     def setUp(self):
#         unittest.TestCase.setUp(self)
# 
#     def tearDown(self):
#         unittest.TestCase.tearDown(self)
#         
#     def testAddInch(self):
#         carte=Carte(12,"Odisea","Homer","clasice")
#         repo_carti=RepositoryCarte()
#         repo_carti.store(carte)
#         persoana=Persoana(15,"Andrei",6)
#         repo_persoane=RepositoryPersoana()
#         repo_persoane.store(persoana)
#         repo_inchirieri=RepositoryInchiriere()
#         self.assertEqual(len(repo_inchirieri), 0,"")
#         inchiriere=Inchiriere(1,12,15)
#         repo_inchirieri.add(inchiriere)
#         self.assertEqual(len(repo_inchirieri),1,"")
#         
#     def testRemInch(self):
#         carte=Carte(12,"Odisea","Homer","clasice")
#         repo_carti=RepositoryCarte()
#         repo_carti.store(carte)
#         persoana=Persoana(15,"Andrei",6)
#         repo_persoane=RepositoryPersoana()
#         repo_persoane.store(persoana)
#         repo_inchirieri=RepositoryInchiriere()
#         self.assertEqual(len(repo_inchirieri), 0,"")
#         inchiriere=Inchiriere(1,12,15)
#         repo_inchirieri.add(inchiriere)
#         key=Inchiriere(1,"","")
#         repo_inchirieri.remove(key)
#         self.assertEqual(len(repo_inchirieri), 0, "")
#          
#         
#         
#     
class FileRepositoryInchiriere(RepositoryInchiriere):


    def __init__(self, filename):
        self.__filename = filename
        RepositoryInchiriere.__init__(self)


    def __citeste_tot_din_fiser(self):
        with open(self.__filename,"r") as f:
            self._elems=[]
            lines=f.readlines()
            for line in lines:
                line=line.strip()
                if line!="":
                    parts=line.split(";")
                    inchi=Inchiriere(int(parts[0]),int(parts[1]),int(parts[2]))
                    self._elems.append(inchi)


    def __append_inchi_in_fisier(self,inchi):
        with open(self.__filename,"a") as f:
            f.write(str(inchi.get_id_i())+';'+str(inchi.get_carte().get_id())+';'+str(inchi.get_client().get_id1())+'\n')
            #f.write(str(inchi.get_id_i())+';'+str(inchi.get_carte())+';'+str(inchi.get_client())+'\n')

    def __scrie_tot_in_fisier(self):
        with open(self.__filename,"w") as f:
            for inchi in self._elems:
                f.write(str(inchi.get_id_i())+';'+str(inchi.get_carte())+';'+str(inchi.get_client())+'\n')




    def add(self, inchiriere):
        self.__citeste_tot_din_fiser()
        RepositoryInchiriere.add(self, inchiriere)
        self.__append_inchi_in_fisier(inchiriere)

    def get_all(self):
        self.__citeste_tot_din_fiser()
        return RepositoryInchiriere.get_all(self)


    def __len__(self):
        self.__citeste_tot_din_fiser()
        return RepositoryInchiriere.__len__(self)


    def remove(self, key):
        self.__citeste_tot_din_fiser()
        RepositoryInchiriere.remove(self, key)

        self.__scrie_tot_in_fisier()


class TestCaseInchRepoFile(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        file = open("inchTeste.txt", "w")
        file.close()

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        file = open("inchTeste.txt", "w")
        file.close()

    def testAddInch(self):
        carte=Carte(12,"Odisea","Homer","clasice")
        repo_carti=FileRepositoryCarte("cartiTeste.txt")
        repo_carti.store(carte)
        persoana=Persoana(15,"Andrei",6)
        repo_persoane=FileRepositroyPersoana("clientiTeste.txt")
        repo_persoane.store(persoana)
        repo_inchirieri=FileRepositoryInchiriere("inchTeste.txt")
        self.assertEqual(len(repo_inchirieri), 0,"")
        i=1
        inchiriere=Inchiriere(i,carte,persoana)
        repo_inchirieri.add(inchiriere)

        self.assertEqual(len(repo_inchirieri),1,"")

    def testRemInch(self):
        carte=Carte(2,"Odisea","Homer","clasice")
        repo_carti=FileRepositoryCarte("cartiTeste.txt")
        repo_carti.store(carte)
        persoana=Persoana(5,"Andrei",6)
        repo_persoane=FileRepositroyPersoana("clientiTeste.txt")
        repo_persoane.store(persoana)
        repo_inchirieri=FileRepositoryInchiriere("inchTeste.txt")
        self.assertEqual(len(repo_inchirieri), 0,"")
        i=1
        inchiriere=Inchiriere(i,carte,persoana)
        repo_inchirieri.add(inchiriere)
        key=Inchiriere(1,"","")
        repo_inchirieri.remove(key)
        self.assertEqual(len(repo_inchirieri), 0, "")

if  __name__ == "__main__":
    unittest.main() 


