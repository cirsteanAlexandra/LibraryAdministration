from domain.entities import Carte,Persoana, Inchiriere
from validation.validators import ValidatorCarte, ValidatorPersoana,ValidatorInchiriere
from errors.exceptions import ValidationException,RepoException
from infrastructure.repositories import RepositoryCarte,RepositoryPersoana,RepositoryInchiriere,\
    FileRepositoryCarte,FileRepositroyPersoana, FileRepositoryInchiriere
from business.services import ServiceCarte,ServicePersoana,ServiceInchiriere
from methods.sort import Sorts


class Tests:
    
    def __run_create_tests_carte(self):
        id=12
        titlu="Idiotul"
        autor="Dostoievsky"
        descriere="clasice"
        carte=Carte(id,titlu,autor,descriere)
        assert(carte.get_id()==12)
        assert(carte.get_titlu()=="Idiotul")
        assert(carte.get_autor()=="Dostoievsky")
        assert(carte.get_descriere()=="clasice")
        assert(str(carte)=="12 Idiotul Dostoievsky clasice")
        carte0=Carte(id,None,None,None)
        assert(carte==carte0)
        return carte
        
        
        
    def __run_create_tests_persoana(self):
         
        id1=13
        nume="Raul"
        cnp=5
        persoana=Persoana(id1,nume,cnp)
        assert(persoana.get_id1()==13)
        assert(persoana.get_nume()=="Raul")
        assert(persoana.get_cnp()==5)
        assert(str(persoana)=="13 Raul 5")
        persoana0=Persoana(id1,None,cnp)
        assert(persoana==persoana0)
        return persoana

        
    
    def __run_validation_tests_carte(self,carte,carte_invalida):
        validator_carti=ValidatorCarte()
        validator_carti.valideaza_c(carte)
        try:
            validator_carti.valideaza_c(carte_invalida)
            assert(False)
        except ValidationException as ve:
            assert(str(ve)=="id invalid!\ntitlu invalid!\nautor invalid!\ndescriere invalida!\n")
#           
#         
#       
#     def __run_repo_tests_carte(self, carte):
#         repo=RepositoryCarte
#         assert(len(repo)==0)
#         repo.store(carte)
#         assert(len(repo)==1)
#         gasit=repo.search(carte.get_id())
#         assert(gasit.get_titlu()==carte.get_titlu())
#         try:
#             repo.store(carte)
#             assert(False)
#         except RepoException as re:
#             assert(str(re)=="element existent!\n")
#         return repo
#     
#     
#     def __run_srv_tests_carte(self, repo, validator_carti):
#         srv=ServiceCarte(repo,validator_carti)
#         id=34
#         titlu="Notre dame de Paris"
#         autor="Victor Hugo"
#         descriere="clasice"
#         srv.add_carte(id, titlu, autor, descriere)
#         assert(srv.get_no_carte()==2)
#         gasit=srv.search_carte(34)
#         assert(gasit.get_titlu()==titlu)
#         try:
#             srv.add_carte(id,titlu,autor,descriere)
#             assert(False)
#         except RepoException as re:
#             assert(srv.get_no_carte()==2)
#             assert(str(re)=="element existent!\n") 
#         
#         try:
#             srv.add_carte(-id,"",autor,descriere)
#             assert(False)
#         except ValidationException as ve:
#             assert(srv.get_no_carte()==2)
#             assert(str(ve)=="id invalid!\ntitlu invalid!\n")
#         
#         
#     
#     def __run_add_tests_carte(self):
#         carte=self.__run_add_tests_carte()
#         carte_invalida=carte=Carte(-12,"","","") 
#         validator_carti=self.__run_validation_tests_carte(carte,carte_invalida)
#         repo=self.__run_repo_tests_carte(carte)
#         srv=self.__run_srv_tests_carte(repo,validator_carti)
#         
        
    def __run_validation_tests_persoana(self):
         
        persoana=Persoana(-15,"",11)
        validator_persoane=ValidatorPersoana()
        try:
            validator_persoane.valideaza_p(persoana)
            assert(False)
        except ValidationException as te:
            assert(str(te)=="id1 invalid!\nnume invalid!\ncnp invalid!\n")
        persoana_valida=Persoana(14,"Radu",4)
        validator_persoane.valideaza_p(persoana_valida)
        assert(True)
     
    def __run_validation_tests_inchiriere(self):
         
        inchiriere=Inchiriere(-15,2,3)
        validator_inchirieri=ValidatorInchiriere()
        try:
            validator_inchirieri.valideaza_i(inchiriere)
            assert(False)
        except ValidationException as te:
            assert(str(te)=="id_i invalid!\n")
        inchiriere_valida=Inchiriere(14,5,4)
        validator_inchirieri.valideaza_i(inchiriere_valida)
        assert(True)
    
    def __run_repository_carte_tests(self):
        carte=Carte(12,"Odisea","Homer","clasice")
        #repo_carti=RepositoryCarte()
        with open(r"C:\Users\Dell\eclipse-workspace\lab7 nou\testing\cartiTeste.txt","w") as f:
            f.write("")
        repo_carti=FileRepositoryCarte(r"C:\Users\Dell\eclipse-workspace\lab7 nou\testing\cartiTeste.txt")
        assert(len(repo_carti)==0)
        repo_carti.store(carte)
        assert(len(repo_carti)==1)
        key_carte=Carte(12,None,None,None)
        result_carte=repo_carti.search(key_carte)
        assert(carte.get_titlu()==result_carte.get_titlu())
        assert(carte.get_autor()==result_carte.get_autor())
        assert(carte.get_descriere()==result_carte.get_descriere())
        carte0=Carte(12,None,None,None)
        try:
            repo_carti.store(carte0)
            assert(False)
        except RepoException as re:
            assert(str(re)=="element existent!\n")
        carte1=Carte(23,"Mos Goriot","Balzac","clasice")
        try:
            repo_carti.update(carte1)
            assert(False)
        except RepoException as re:
            assert(str(re)=="element inexistent!\n")
              
        carte2=Carte(12,"Poezii","Bacovia","literatura romana")
        repo_carti.update(carte2)
        result_carte=repo_carti.search(key_carte)
        assert("Poezii"==result_carte.get_titlu())
        assert("Bacovia"==result_carte.get_autor())
        assert("literatura romana"==result_carte.get_descriere())
          
        repo_carti.remove(key_carte)
        assert(len(repo_carti)==0)
        try:
            repo_carti.remove(key_carte)
            assert(False)
        except RepoException as re:
            assert(str(re)=="element inexistent!\n")
              
        carte3=Carte(13,"Poezii","Bacovia","literatura romana")  
        assert(len(repo_carti)==0)
        repo_carti.store(carte3)
        assert(len(repo_carti)==1)
         
        
  
    def __run_repository_persoana_tests(self):  
     # pass
        persoana=Persoana(15,"Andrei",6)
        #repo_persoane=RepositoryPersoana()
        with open(r"C:\Users\Dell\eclipse-workspace\lab7 nou\testing\clientiTeste.txt","w") as f:
            f.write("")
        repo_persoane=FileRepositroyPersoana(r"C:\Users\Dell\eclipse-workspace\lab7 nou\testing\clientiTeste.txt") 
        assert(len(repo_persoane)==0)
        repo_persoane.store(persoana)
        assert(len(repo_persoane)==1)
        key_persoane=Persoana(15,None,None)
        result_persoane=repo_persoane.search(key_persoane)
        assert(persoana.get_nume()==result_persoane.get_nume())
        assert(persoana.get_cnp()==result_persoane.get_cnp())
         
        persoana0=Persoana(15,None,None)
        try:
            repo_persoane.store(persoana0)
            assert(False)
        except RepoException as re:
            assert(str(re)=="element existent!\n")
             
        persoana1=Persoana(23,"Vlad",6)
        try:
            repo_persoane.update(persoana1)
            assert(False)
        except RepoException as re:
            assert(str(re)=="element inexistent!\n")
             
        persoana2=Persoana(15,"Cosmin",6)
        repo_persoane.update(persoana2)
        result_persoane=repo_persoane.search(key_persoane)
        assert("Cosmin"==result_persoane.get_nume())
        assert(6==result_persoane.get_cnp())
         
        repo_persoane.remove(key_persoane)
        assert(len(repo_persoane)==0)
        try:
            repo_persoane.remove(key_persoane)
            assert(False)
        except RepoException as re:
            assert(str(re)=="element inexistent!\n")
              
        persoana3=Persoana(17,"Cosmin",6)
        assert(len(repo_persoane)==0)
        repo_persoane.store(persoana3)
        assert(len(repo_persoane)==1)
          
         
         
             
    def __run_repository_inchiriere_test(self):   
        carte=Carte(12,"Odisea","Homer","clasice")
        
        repo_carti=RepositoryCarte()
        #repo_carti=FileRepositoryCarte(r"C:\Users\Dell\eclipse-workspace\lab7 nou\testing\cartiTeste.txt")
        repo_carti.store(carte)
        persoana=Persoana(15,"Andrei",6)
        repo_persoane=RepositoryPersoana()
        #repo_persoane=FileRepositroyPersoana(r"C:\Users\Dell\eclipse-workspace\lab7 nou\testing\clientiTeste.txt")
        repo_persoane.store(persoana)
        repo_inchirieri=RepositoryInchiriere()
        #repo_inchirieri=FileRepositoryInchiriere(r"C:\Users\Dell\eclipse-workspace\lab7 nou\testing\inchTeste.txt")
        assert(len(repo_inchirieri)==0)
        inchiriere=Inchiriere(1,12,15)
        repo_inchirieri.add(inchiriere)
        assert(len(repo_inchirieri)==1)
        key=Inchiriere(1,"","")
        repo_inchirieri.remove(key)
        assert(len(repo_inchirieri)==0)
         
    def __run_service_carte_tests(self):
        repo_carti=RepositoryCarte()
        valid_carti=ValidatorCarte()
        service_carte=ServiceCarte(repo_carti,valid_carti)
        id=34
        titlu="Notre dame de Paris"
        autor="Victor Hugo"
        descriere="clasice"
        service_carte.add_carte(id,titlu,autor,descriere)
        assert(service_carte.get_no_carte()==1)
        try:
            service_carte.add_carte(id,titlu,autor,descriere)
            assert(False)
        except RepoException as re:
            assert(str(re)=="element existent!\n") 
        try:
            service_carte.add_carte(-id,"",autor,descriere)
            assert(False)
        except ValidationException as ve:
            assert(str(ve)=="id invalid!\ntitlu invalid!\n")
             
#         key_carte="1984"
#          
#         try:
#             result_carte=service_carte.search_carte_by_titlu(key_carte)
#             assert(False)
#         except RepoException as re:
#             assert(str(re)=="nu exista carti cu acest titlu! ")
#               
#         key_carte="Victor Hugo"
#         result_carte=service_carte.search_carte_by_autor(key_carte)
#         assert(result_carte[0].get_autor()=="Victor Hugo")
#         assert(result_carte[0].get_id()==34)
#         assert(result_carte[0].get_descriere()=="clasice")
#         assert(result_carte[0].get_titlu()=="Notre dame de Paris")
# #         
#         key_carte="Blaga"
#           
#         try:
#             result_carte=service_carte.search_carte_by_autor(key_carte)
#             assert(False)
#         except RepoException as re:
#             assert(str(re)=="nu exista carti de acest autor! ")
#               
#         key_carte="clasice"
#         result_carte=service_carte.search_carte_by_descriere(key_carte)
#         assert(result_carte[0].get_autor()=="Victor Hugo")
#         assert(result_carte[0].get_id()==34)
#         assert(result_carte[0].get_descriere()=="clasice")
#         assert(result_carte[0].get_titlu()=="Notre dame de Paris")
#           
#         key_carte="literatura romana"
#           
#         try:
#             result_carte=service_carte.search_carte_by_descriere(key_carte)
#             assert(False)
#         except RepoException as re:
#             assert(str(re)=="nu exista carti cu aceasta descriere! ")
# #            
         
             
    def __run_service_persoane_tests(self):
        repo_persoane=RepositoryPersoana()
        valid_persoana=ValidatorPersoana()
        service_persoana=ServicePersoana(repo_persoane,valid_persoana)
        id1=34
        nume="Victor"
        cnp=1
        service_persoana.add_persoana(id1, nume, cnp)
        assert(service_persoana.get_no_persoane()==1)
        try:
            service_persoana.add_persoana(id1, nume, cnp)
            assert(False)
        except RepoException as re:
            assert(str(re)=="element existent!\n") 
        try:
            service_persoana.add_persoana(-id1,"", cnp)
            assert(False)
        except ValidationException as ve:
            assert(str(ve)=="id1 invalid!\nnume invalid!\n")
             
             
        key_persoane="Victor"
        result_persoane=service_persoana.search_persoana_nume(key_persoane)
        assert(result_persoane[0].get_nume()=="Victor")
        assert(result_persoane[0].get_cnp()==1)
        assert(result_persoane[0].get_id1()==34)
         
        key_persoane="Cosmin"
        try:
            result_persoane=service_persoana.search_persoana_nume(key_persoane)
            assert(False)
        except RepoException as ve:
            assert(str(ve)=="nu exista  clienti cu acest nume! ")
         
        key_persoane=1
        result_persoane=service_persoana.search_persoana_cnp(key_persoane)
        assert(result_persoane[0].get_nume()=="Victor")
        assert(result_persoane[0].get_cnp()==1)
        assert(result_persoane[0].get_id1()==34)
             
     
     
    def __run_service_inchiriere_test(self):
        
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
        assert(service_inchirieri.get_no_inchirieri()==1)
        try:
            service_inchirieri.add_inchiriere(id_i, id_carte,id_client)
            assert(False)
        except RepoException as re:
            assert(str(re)=="element existent!") 
             
        id=35
        titlu="Notre dame de Paris"
        autor="Victor Hugo"
        descriere="clasice"
        service_carte.add_carte(id,titlu,autor,descriere)
        id1=30
        nume="Matei"
        cnp=1
        service_persoana.add_persoana(id1, nume, cnp)
        id_i=2
        id_carte=35
        id_client=30
        service_inchirieri.add_inchiriere(id_i, id_carte,id_client)
        assert(len(repo_inchiriere)==2)
        
#        
        
        m=[['cosmin', 3], ['vlad', 2], ['andrei', 1]]
        li=sort.shak_sort(m,reversed=True)
        assert(li==[['vlad', 2], ['cosmin', 3], ['andrei', 1]])
#         
        m1=[['cosmin', 3], ['vlad', 2], ['andrei', 1]]
        l1=sort.shak_sort(m1)
        assert(l1==[['andrei', 1], ['cosmin', 3], ['vlad', 2]])
#         
        m2=[['cosmin', 3], ['vlad', 2], ['andrei', 1]]
        l2=sort.selection_sort(m2)
        assert(l2==[['andrei', 1], ['cosmin', 3], ['vlad', 2]])
         
        m3=[['cosmin', 3], ['vlad', 2], ['andrei', 1]]
        l3=sort.selection_sort(m3,reversed=True)
        assert(l3==[['vlad', 2], ['cosmin', 3], ['andrei', 1]])
         
        m4=[['cosmin', 3], ['vlad', 2], ['andrei', 1]]
        l4=sort.shak_sort(m4,lambda l,x:l[x][1])
        assert(l4==[['andrei', 1], ['vlad', 2], ['cosmin', 3]])
         
        m5=[['cosmin', 3], ['vlad', 2], ['andrei', 1]]
        l5=sort.shak_sort(m5,lambda l,x:l[x][1],reversed=True)
        assert(l5==[['cosmin', 3], ['vlad', 2], ['andrei', 1]])
#          
        m6=[['cosmin', 3], ['vlad', 2], ['andrei', 1]]
        l6=sort.selection_sort(m6,lambda l,x:l[x][1])
        assert(l6==[['andrei', 1], ['vlad', 2], ['cosmin', 3]])
          
        m7=[['cosmin', 3], ['vlad', 2], ['andrei', 1]]
        l7=sort.selection_sort(m7,lambda l,x:l[x][1],reversed=True)
        assert(l7==[['cosmin', 3], ['vlad', 2], ['andrei', 1]])
#         
        
    
    def run_all_tests(self):
        self.__run_create_tests_carte()
        self.__run_create_tests_persoana()
         
        #self.__run_validation_tests_carte()
        self.__run_validation_tests_persoana()
        self.__run_validation_tests_inchiriere()
         
        self.__run_repository_carte_tests()
        #self.__run_repository_persoana_tests()
         
        self.__run_service_carte_tests()
        self.__run_service_persoane_tests()
        
        self.__run_repository_inchiriere_test()
        self.__run_service_inchiriere_test()
        
        

