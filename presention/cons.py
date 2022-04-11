from errors.exceptions import ValidationException, RepoException
from domain.entities import Carte,Persoana,Inchiriere
from methods.sort import Sorts

class UI:

    
    def __ui_add_carte(self):
        id=int(input("inroduceti id carte: "))
        titlu= input("introduceti titlu: ")
        autor=input("introducei autor: ")
        descriere=input("introduceti descriere: ")
        self.__service_carti.add_carte(id,titlu,autor,descriere)
        
    
    def __ui_print_carti(self):
        carti=self.__service_carti.get_carti()
        if len(carti)==0:
            print("nu exista carti")
            return
        for carte in carti:
           print(carte)
    
    
    def __ui_remove_carti(self):
        carti=self.__service_carti.get_carti()
        if len(carti)==0:
            print("nu exista carti")
            return
        print("adauga id cartii pe care vrei sa o stergi ")
        key=int(input(" "))
        self.__service_inchirieri.remove_inchirieri_by_id_carte(key)
        self.__service_carti.remove_carte(key)
        
                
    def __ui_search_carte(self):
        carti=self.__service_carti.get_carti()
        if len(carti)==0:
            print("nu exista carti")
            return
        cauta=input("adauga camp: ")
        if cauta=="id":
            print("adauga id carte pe care o cauti ")
            key=int(input(" "))
            print(self.__service_carti.search_carte(key))
            return
            
        if cauta=="titlu":
            x=[]
            y=[]
            print("adauga titlul pe care vrei sa l cauti: ")
            key=input(" ")
            x=self.__service_carti.search_carte_by_titlu(key,carti,y)
           
            for i in range(len(x)):
                print(x[i])
            return
        
                
        if cauta=="autor":
            x=[]
            y=[]
#             
            print("adauga autorul pe care vrei sa l cauti: ")
            key=input(" ")
            x=self.__service_carti.search_carte_by_autor(key,carti,y)
            for i in range(len(x)):
                print(x[i])
            return
        
        if cauta=="descriere":
            x=[]
            print("adauga descrierea pe care vrei sa o cauti: ")
            key=input(" ")
            x=self.__service_carti.search_carte_by_descriere(key)
            for i in range (len(x)):
                print(x[i])
            return
        print("camp invalid! ")
        return
                
    
    def __ui_update_carti(self):
        carti=self.__service_carti.get_carti()
        if len(carti)==0:
            print("nu exista carti")
            return
        print("adauga id cartii pe care vrei sa o modifici ")
        key=int(input(" "))
        carte=self.__service_carti.search_carte(key)
        print("ce vrei sa modifici? ")
        mod=input("")
        if mod=="titlu":
            new=input("noul titlu este: ")
            carte.set_titlu(new)
        if mod=="autor":
            new=input("noul autor este: ")
            carte.set_autor(new)
        if mod=="descriere":
            new=input("noua descriere este: ")
            carte.set_descriere(new)
            
        self.__service_carti.update_carte(carte)    
        
    
    def __ui_add_persoane(self):
        id1=int(input("introdu id client: "))
        nume=input("introdu numele: ")
        cnp=int(input("introdu cnp: "))
        self.__service_persoane.add_persoana(id1,nume,cnp)
    
    def __ui_print_persoane(self):
        persoane=self.__service_persoane.get_persoane()
        if len(persoane)==0:
            print("nu exista clienti")
            return
        for persoana in persoane:
            print(persoana)
    
    def __ui_remove_persoane(self):
        persoane=self.__service_persoane.get_persoane()
        if len(persoane)==0:
            print("nu exista clienti")
            return
        print("introdu id clientului pe care vrei sa l stergi ")
        key=int(input(" "))
        self.__service_inchirieri.remove_persoana_by_id(key)
        self.__service_persoane.remove_persoana(key)
        
    def __ui_update_persoane(self):
        persoane=self.__service_persoane.get_persoane()
        if len(persoane)==0:
            print("nu exista clienti! ")
            return
        print("adauga id clientului pe care vrei sa l modifici")
        key=int(input(""))
        persoana=self.__service_persoane.search_persoana(key)
        print("ce vrei sa modifici? ")
        mod=input()
        if mod=="nume":
            print("adauga noul nume: ")
            new=input("")
            persoana.set_nume(new)
        if mod=="cnp":
            print("noul cnp este: ")
            new=int(input(""))
            persoana.set_cnp(new)
            
        self.__service_persoane.update_persoana(persoana)
    
    def __ui_search_persoane(self):
        persoane=self.__service_persoane.get_persoane()
        if len(persoane)==0:
            print("nu exista clienti! ")
            return
        cauta=input("adauga campul: ")
        if cauta=="id":
            print("adauga id: ")
            key=int(input(""))
            print(self.__service_persoane.search_persoana(key))
            return
        if cauta=="nume":
            x=[]
            print("adauga numele: ")
            key=input(" ")
            x=self.__service_persoane.search_persoana_nume(key)
            for i in range(len(x)):
                print(x[i])
            return
        if cauta=="cnp":
            x=[]
            print("adauga cnp: ")
            key=int(input(" "))
            x=self.__service_persoane.search_persoana_cnp(key)
            for i in range(len(x)):
                print(x[i])
            return 
        print("camp invalid! ")
        return
        
    def __ui_add_inchiriere(self):
        id_i=int(input("adauga id inchirierii: "))
        id_carte=int(input("adauga id cartii:"))
        id_client=int(input("adauga id clientului: "))
        
        self.__service_inchirieri.add_inchiriere(id_i,id_carte,id_client)
    
    
    def __ui_print_inchirieri(self):

        inchirieri=self.__service_inchirieri.get_all_inchirieriFisier()
        if len(inchirieri)==0:
            print("nu exista inchirieri! ") 
            return
        for inchiriere in inchirieri:
            print(inchiriere)
    
    
    def __ui_remove_inchiriere(self):
        #pass
        inchirieri=self.__service_inchirieri.get_all_inchirieri()
        if len(inchirieri)==0:
            print("nu exista inchirieri! ") 
            return
        id=int(input("adauga  id inchiriere: "))
        self.__service_inchirieri.remove_inchiriere_by_id(id)
    
        
    def __id_unic(self,id):
        key=id
        try:
            self.__service_carti.search_carte(key)
        except RepoException as re:
            assert(str(re)=="element inexistent!\n")
            return 1
        return 0
        
    def __ui_get_random_id(self):
        import random
        x=random.randint(1,100) 
        if self.__id_unic(x)==0:
            return self.__ui_get_random_id()
        return x
    
    def __ui_add_random_carti(self,param):
        import random
        if len(param)<1:
            print("parametru invalid! ")
            return 
        x=param[0]+param[1]
        for i in range(int(x)):
            string="abcdefghijklmnopqrst"
            x=self.__ui_get_random_id()    
            id=x    
            y=random.randint(1,20)
            letters = "abcdefghijklmnopqrstz"
            titlu = ''.join(random.choice(letters) for i in range(y))
            y=random.randint(1,20)
            letters = "abcdefghijklmnopqrstz"
            autor = ''.join(random.choice(letters) for i in range(y))
            y=random.randint(1,20)
            letters = "abcdefghijklmnopqrstz"
            descriere = ''.join(random.choice(letters) for i in range(y))
            self.__service_carti.add_carte(id,titlu,autor,descriere)  
    
    
    def __id_unicp(self,id):
        key=id
        try:
            self.__service_persoane.search_persoana(key)
        except RepoException as re:
            assert(str(re)=="element inexistent!\n")
            return 1
        return 0
        
        
    
    def __ui_get_random_idp(self):
        import random
        x=random.randint(1,100) 
        if self.__id_unicp(x)==0:
            return self.__ui_get_random_idp()
        return x
    
    
    def __ui_add_random_persoane(self,para):
        import random
        if len(para)<1:
            print("parametru invalid! ")
            return 
        l=para[0]+para[1]
       
        for i in range(int(l)):
            string="abcdefghijklmnopqrst"
            x=self.__ui_get_random_idp()
            id1=x
            y=random.randint(1,20)
            letters = "abcdefghijklmnopqrstz"
            nume = ''.join(random.choice(letters) for i in range(y))
            y=random.randint(1,9)
            cnp =y
            self.__service_persoane.add_persoana(id1,nume,cnp) 

    def __ui_rapoarte_carti(self):
        rezult=self.__service_inchirieri.cele_mai_inchiriate()
        if len(rezult)<1:
            print("nu exista inchirieri! ")
            return
        print("cea/cele mai inchiriata(e) carti sunt: ")
        for i in range(len(rezult)):
            print(rezult[i])
            
    def __ui_rapoarte_clienti(self):

        rez=self.__service_inchirieri.sort_clienti_by_nume()
        for i in range(len(rez)):
            print(rez[i][0]," nr de carti inchiriate ",rez[i][1])

    def __init__(self, service_carti,service_persoane,service_inchirieri):
        
        self.__service_carti=service_carti
        self.__service_persoane=service_persoane
        self.__service_inchirieri=service_inchirieri
        self.__comenzi={
            "add_carte":self.__ui_add_carte,
            "print_carti":self.__ui_print_carti,
            "update_carti":self.__ui_update_carti,
            "add_client":self.__ui_add_persoane,
            "print_clienti":self.__ui_print_persoane,
            "update_clienti":self.__ui_update_persoane,
            "remove_carte": self.__ui_remove_carti,
            "remove_client":self.__ui_remove_persoane,
            "search_carte":self.__ui_search_carte,
            "search_client": self.__ui_search_persoane,
            "add_inch": self.__ui_add_inchiriere,
            "print_inch":self.__ui_print_inchirieri,
            "remove_inch":self.__ui_remove_inchiriere,
        
            "test":self.__ui_get_random_id,
            "rapoarte_carti":self.__ui_rapoarte_carti,
            "r":self.__ui_rapoarte_clienti,

            }
    
    def run(self):
        while True:
            cmd=input("adauga comanda: ")
            if cmd=="exit":
               print("bye")
               return
            if cmd.startswith('add_random_carti'):
                x=cmd[len(cmd)-2]+cmd[len(cmd)-1]
                self.__ui_add_random_carti(x)
                cmd=input("adauga comanda: ")
            if cmd.startswith('add_random_clienti'):
               x=cmd[len(cmd)-2]+cmd[len(cmd)-1]
               self.__ui_add_random_persoane(x)
               cmd=input("adauga comanda: ")
             
            if cmd in self.__comenzi:
                try:
                    self.__comenzi[cmd]()
                except ValueError:
                    print("valoare numerica invalida!")  
                except ValidationException as ve:
                    print(ve)
                except RepoException as re:
                    print(re)   
            else: print("comanda invalida")   
#     
    



