from domain.entities import Carte,Persoana,Inchiriere,InchiriereDTO
from errors.exceptions import RepoException,ValidationException
from infrastructure.repositories import RepositoryCarte,RepositoryPersoana,RepositoryInchiriere
from validation.validators import ValidatorCarte,ValidatorPersoana,ValidatorInchiriere
import unittest
from methods.sort import Sorts
class ServiceCarte:

    def __init__(self, repo_carti,valid_carti):
        self.__repo_carti=repo_carti
        self.__valid_carti=valid_carti
       
        carti=self.__repo_carti.get_all()
        

    
    def add_carte(self, id, titlu, autor, descriere):
        carte=Carte(id,titlu,autor,descriere)
        self.__valid_carti.valideaza_c(carte)
        self.__repo_carti.store(carte)

    def get_no_carte(self):
        return len(self.__repo_carti)

    def get_carti(self):
        return self.__repo_carti.get_all()
    
    def update_carte(self,carte):
        self.__valid_carti.valideaza_c(carte)
        self.__repo_carti.update(carte)
    
    def remove_carte(self,key):
        carte=Carte(key,"","","")
        self.__repo_carti.remove(carte)
        
    def search_carte(self,key):
        carte=Carte(key,"","","")
        return self.__repo_carti.search(carte)
    
    def search_carte_by_titlu(self,carte_titlu,carti,cartit):
        if len(carti)==0:
            if len(cartit)==0:
                raise RepoException("nu exista carti cu acest titlu! ")
            else: return cartit
        
        if carti[0].get_titlu()==carte_titlu:
                cartit.append(carti[0])
                
        return self.search_carte_by_titlu(carte_titlu, carti[1:], cartit)
        
#     def search_carte_by_titlu(self,carte_titlu):
#         cartit=[]
#         carti=self.__repo_carti.get_all()
#         for carte in carti:
#             if carte.get_titlu()==carte_titlu:
#                 cartit.append(carte)
#                
#         if len(cartit)!=0: return cartit
#         raise RepoException("nu exista carti cu acest titlu! ")
    
#     def search_carte_by_autor(self,carte_autor):
#         carti=self.__repo_carti.get_all()
#         cartia=[]
#         for carte in carti:
#             if carte.get_autor()==carte_autor:
#                 cartia.append(carte)
#         if len(cartia)!=0: return cartia
#         raise RepoException("nu exista carti de acest autor! ")
    
    def search_carte_by_autor(self,carte_autor,carti,cartia):
        
        if len(carti)==0: 
            if len(cartia)==0:
                raise RepoException("nu exista carti de acest autor! ")
            else: return cartia
        
        if carti[0].get_autor()==carte_autor:
                cartia.append(carti[0])
        
        return self.search_carte_by_autor(carte_autor,carti[1:],cartia)
       
       
    
    
    def search_carte_by_descriere(self,carte_descriere):
        cartid=[]
        carti=self.__repo_carti.get_all()
        for carte in carti:
            if carte.get_descriere()==carte_descriere:
                cartid.append(carte)
        if len(cartid)!=0: return cartid
        raise RepoException("nu exista carti cu aceasta descriere! ")
    
class TestCaseCartiServ(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testSearchCarte(self):
        repo_carti=RepositoryCarte()
        valid_carti=ValidatorCarte()
        service_carte=ServiceCarte(repo_carti,valid_carti)
        id=34
        titlu="Notre dame de Paris"
        autor="Victor Hugo"
        descriere="clasice"
        service_carte.add_carte(id,titlu,autor,descriere)
        
        l=repo_carti.get_all()
        key_carte="1984"
        c=[]
        try:
            result_carte=service_carte.search_carte_by_titlu(key_carte,l,c)
            self.assertFalse(False, "CARTE INEXISTENTA")
        except RepoException as re:
            self.assertEqual(str(re),"nu exista carti cu acest titlu! " ,"")
        n=[]
        l=repo_carti.get_all()   
        key_carte="Victor Hugo"
        result_carte=service_carte.search_carte_by_autor(key_carte,l,n)
        self.assertEqual(result_carte[0].get_autor(), "Victor Hugo", "")
        self.assertEqual(result_carte[0].get_id(), 34, "")
        self.assertEqual(result_carte[0].get_descriere(), "clasice", "")
        self.assertEqual(result_carte[0].get_titlu(), "Notre dame de Paris", "")
        o=[]
        key_carte="Blaga"
          
        try:
            result_carte=service_carte.search_carte_by_autor(key_carte,l,o)
            self.assertFalse(False, "CARTE INEXISTENTA")
        except RepoException as re:
            self.assertEqual(str(re),"nu exista carti de acest autor! ")
              
        key_carte="clasice"
        result_carte=service_carte.search_carte_by_descriere(key_carte)
        self.assertEqual(result_carte[0].get_autor(), "Victor Hugo", "")
        self.assertEqual(result_carte[0].get_id(), 34, "")
        self.assertEqual(result_carte[0].get_descriere(), "clasice", "")
        self.assertEqual(result_carte[0].get_titlu(), "Notre dame de Paris", "")
          
        key_carte="literatura romana"
          
        try:
            result_carte=service_carte.search_carte_by_descriere(key_carte)
            self.assertFalse(False, "DEASCRIERE INEXISTENTA")
        except RepoException as re:
            self.assertEqual(str(re),"nu exista carti cu aceasta descriere! " , "")


class ServicePersoana:
    
    def __init__(self,repo_persoane,valid_persoane):
        self.__repo_persoane=repo_persoane
        self.__valid_persoane=valid_persoane
        
    
    def add_persoana(self, id1,nume,cnp):
        persoana=Persoana(id1,nume,cnp)
        self.__valid_persoane.valideaza_p(persoana)
        self.__repo_persoane.store(persoana)

    def update_persoana(self,persoana):
        self.__valid_persoane.valideaza_p(persoana)
        self.__repo_persoane.update(persoana)
        
    def get_no_persoane(self):
        return len(self.__repo_persoane)

    def get_persoane(self):
        return self.__repo_persoane.get_all()
    
    def remove_persoana(self,key):
        persoana=Persoana(key,"",None)
        self.__repo_persoane.remove(persoana)
    
    def search_persoana(self,key):
        persoana=Persoana(key,"","")
        return self.__repo_persoane.search(persoana)
    
    
    def search_persoana_nume(self,client_nume):
        clientin=[]
        clienti=self.__repo_persoane.get_all()
        for client in clienti:
            if client.get_nume()==client_nume:
                clientin.append(client)
        if len(clientin)!=0: return clientin
        raise RepoException("nu exista  clienti cu acest nume! ")
    
    def search_persoana_nume1(self,nume):
        clienti=self.__repo_persoane.get_all()
        for client in clienti:
            if client.get_nume()==nume:
                return client
        raise RepoException("nu exista  clineti cu acest nume! ")
    
    def search_persoana_cnp(self,client_cnp):
        clientic=[]
        clienti=self.__repo_persoane.get_all()
        for client in clienti:
            if client.get_cnp()==client_cnp:
                clientic.append(client)
        if len(clientic)!=0: return clientic
        raise RepoException("nu exista niciun client cu acest cnp! ")
    
class TestCasePersoaneServ(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    def testSearchPer(self):
        repo_persoane=RepositoryPersoana()
        valid_persoana=ValidatorPersoana()
        service_persoana=ServicePersoana(repo_persoane,valid_persoana)
        id1=34
        nume="Victor"
        cnp=1
        service_persoana.add_persoana(id1, nume, cnp)
        try:
            service_persoana.add_persoana(id1, nume, cnp)
            self.assertFalse(False, "CLIENT INEXISTENT")
        except RepoException as re:
            self.assertEqual(str(re), "element existent!\n", "")
        try:
            service_persoana.add_persoana(-id1,"", cnp)
            self.assertFalse(False, "CLIENT INEXISTENT")
        except ValidationException as ve:
            self.assertEqual(str(ve),"id1 invalid!\nnume invalid!\n", "")
             
             
        key_persoane="Victor"
        result_persoane=service_persoana.search_persoana_nume(key_persoane)
        self.assertEqual(result_persoane[0].get_nume(),"Victor", "")
        self.assertEqual(result_persoane[0].get_cnp(), 1, "")
        self.assertEqual(result_persoane[0].get_id1(), 34, "")
         
        key_persoane="Cosmin"
        try:
            result_persoane=service_persoana.search_persoana_nume(key_persoane)
            self.assertFalse(False, "NUME INEXISTENT")
        except RepoException as ve:
            self.assertEqual(str(ve), "nu exista  clienti cu acest nume! ", "")
         
        key_persoane=1
        result_persoane=service_persoana.search_persoana_cnp(key_persoane)
        self.assertEqual(result_persoane[0].get_nume(), "Victor", '')
        self.assertEqual(result_persoane[0].get_cnp(),1,"")
        self.assertEqual(result_persoane[0].get_id1(),34,"")
             
    
class ServiceInchiriere:
    
    def __init__(self,repo_inchiriere,valid_inchiriere,repo_carti,repo_persoane,sort):
        
        self.__repo_inchiriere=repo_inchiriere
        self.__valid_inchiriere=valid_inchiriere
        self.__repo_carti=repo_carti
        self.__repo_persoane=repo_persoane
        self.__sort=sort
        
        
#     def sort_by_name(self,lista,i):
#         return lista[i][0]  
#      
#     def sort_by_inch(self,lista,i):
#         return lista[i][1]
      
    def get_no_inchirieri(self):
        return len(self.__repo_inchiriere)
        
    def add_inchiriere(self,id_i,id_carte,id_client):
        inchirieri=self.__repo_inchiriere.get_all()
        
        carte=self.__repo_carti.get_carte_by_id(id_carte)
        
        #for inch  in inchirieri:
           # if inch.get_carte().get_id()==carte.get_id(): 
                #raise RepoException("cartea indisponibila! ")
        #carte=self.__repo_carti.get_carte_by_id(id_carte)
        client=self.__repo_persoane.get_client_by_id(id_client)
        
        inchiriere=Inchiriere(id_i,carte,client)
        
        self.__valid_inchiriere.valideaza_i(inchiriere)
        self.__repo_inchiriere.add(inchiriere)
        
    def get_all_inchirieri(self):
        inchirieri=self.__repo_inchiriere.get_all()
        inchirieri_dtos=[]
        
        for inchiriere in inchirieri:
            id_inchiriere=inchiriere.get_id_i()
            carte=inchiriere.get_carte()
            client=inchiriere.get_client()
            inchiriere_dto=InchiriereDTO(id_inchiriere,carte,client)
            inchirieri_dtos.append(inchiriere_dto)
        return inchirieri_dtos
         
    def get_all_inchirieriFisier(self):
        inchirieri=self.__repo_inchiriere.get_all()
        inchirieri_dtos=[]
        for inchiriere in inchirieri:
            id_inchiriere=inchiriere.get_id_i()
            x=inchiriere.get_carte()
            carte=self.__repo_carti.get_carte_by_id(x)
            x=inchiriere.get_client()
            client=self.__repo_persoane.get_client_by_id(x)
            inchiriere_dto=InchiriereDTO(id_inchiriere,carte,client)
            inchirieri_dtos.append(inchiriere_dto)
        return inchirieri_dtos
            
        
    
    def remove_inchirieri_by_id_carte(self,id_carte):
        #pass
        inchirieri=self.__repo_inchiriere.get_all()
         
        for inchiriere in inchirieri:
            #if inchiriere.get_carte().get_id()==id_carte: memorie
           
            if inchiriere.get_carte()==id_carte:
                self.__repo_inchiriere.remove(inchiriere)
                
           #

       
    def remove_persoana_by_id(self,id_persoana):
        inchirieri=self.__repo_inchiriere.get_all()
        for inchiriere in inchirieri:
            #if inchiriere.get_client().get_id1()==id_persoana: memorie
            if inchiriere.get_client()==id_persoana:
                self.__repo_inchiriere.remove(inchiriere)        
        
    def remove_inchiriere_by_id(self,key):
        inchiriere=Inchiriere(key,None,None)
        #print("yes")
        self.__repo_inchiriere.remove(inchiriere)
                 
  
    def cele_mai_inchiriate(self):
        carte=[]
        inchi={}
        rez=[]
        inchirieri=self.__repo_inchiriere.get_all()
        for i in inchirieri:
            #car=i.get_carte().get_id() memorie
            car=i.get_carte()
            if car in inchi:
                inchi[car]+=1
            else:
                inchi[car]=1
        m=max(inchi.values())
        for key,values in inchi.items():
            if inchi[key]==m: 
                v=self.__repo_carti.get_carte_by_id(key)
                rez.append(v)
        return rez
            
    def sort_clienti_by_nume(self):
        inchi={}
        r=[]
        l=[]
        inchirieri=self.__repo_inchiriere.get_all()
        for i in inchirieri:
            #cl=i.get_client().get_nume() memorie
            cl=self.__repo_persoane.get_client_by_id(i.get_client()).get_nume()
            #cl=self.__repo_persoane.get_client_by_id(i.get_client())
            if   cl in inchi:
                inchi[cl]+=1
            else :
                inchi[cl]=1
                
        #return inchi
        for i in inchi:
            l=[]
            l.append(i)
            l.append(inchi[i])
            r.append(l)
        #print(r)
        #li=self.__sort.selection_sort(r) 
       # li=self.__sort.selection_sort(r,lambda l,x:l[x][1])
        #li=self.__sort.selection_sort(r,reversed=True) 
        #li=self.__sort.selection_sort(r,lambda l,x:l[x][1],reversed=True)
        
        #li=self.__shak_sort(r) 
        #li=self.__shak_sort(r,lambda l,x:l[x][1])
        #li=self.__shak_sort(r,reversed=True) 
        #li=self.__shak_sort(r,lambda l,x:l[x][1],reversed=True)
         
         
        
        #li=self.__sort.selection_sort2(r)
        li=self.__sort.selection_sort2(r,reversed=True)
        
        return li
    
    def sort_clienti_by_inch(self):
        inchi={}
        r=[]
        l=[]
        inchirieri=self.__repo_inchiriere.get_all()
        for i in inchirieri:
            #cl=i.get_client().get_nume() memorie
            cl=self.__repo_persoane.get_client_by_id(i.get_client()).get_nume()
            #cl=self.__repo_persoane.get_client_by_id(i.get_client())
            if   cl in inchi:
                inchi[cl]+=1
            else :
                inchi[cl]=1
                 
        #return inchi
        for i in inchi:
            l=[]
            l.append(i)
            l.append(inchi[i])
            r.append(l)
        #li=self.__sort.selection_sort(r,self.__sort.sort_by_inch,True) 
        li=self.__sort.shak_sort(r,self.__sort.sort_by_inch,True) 
         
        return li
     
     

            
class TestCaseInchServ(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testSrv(self):
        repo_carti=RepositoryCarte()
        valid_carti=ValidatorCarte()
        service_carte=ServiceCarte(repo_carti,valid_carti)
         
        repo_persoane=RepositoryPersoana()
        valid_persoana=ValidatorPersoana()
        service_persoana=ServicePersoana(repo_persoane,valid_persoana)
        repo_inchiriere=RepositoryInchiriere()
        valid_inchiriere=ValidatorInchiriere()
        sort=Sorts()
        service_inchirieri=ServiceInchiriere(repo_inchiriere,valid_inchiriere,repo_carti,repo_persoane,sort)
        
        id=34
        titlu="Notre dame de Paris"
        autor="Victor Hugo"
        descriere="clasice"
        service_carte.add_carte(id,titlu,autor,descriere)
         
        id1=34
        nume="Victor"
        cnp=1
        service_persoana.add_persoana(id1, nume, cnp)
         
        id_i=1
        id_carte=34
        id_client=34
         
        service_inchirieri.add_inchiriere(id_i, id_carte,id_client)
        self.assertEqual(service_inchirieri.get_no_inchirieri(),1,"")
        try:
            service_inchirieri.add_inchiriere(id_i, id_carte,id_client)
            self.assertFalse(False, "")
        except RepoException as re:
            self.assertEqual(str(re),"element existent!" , "") 
             
#         

if  __name__ == "__main__":
    unittest.main() 
