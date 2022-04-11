from domain.entities import Carte,Persoana,Inchiriere,InchiriereDTO
from errors.exceptions import RepoException

class ServiceCarte:

    def __init__(self, repo_carti,valid_carti):
        self.__repo_carti=repo_carti
        self.__valid_carti=valid_carti

    
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
    
    def search_carte_by_titlu(self,key):
        carte=Carte(None,key,"","")
        return self.__repo_carti.get_carte_by_titlu(carte)
    
    def search_carte_by_autor(self,key):
        carte=Carte(None,"",key,"")
        return self.__repo_carti.get_carte_by_autor(carte)
    
    def search_carte_by_descriere(self,key):
        carte=Carte(None,"","",key)
        return self.__repo_carti.get_carte_by_descriere(carte)
    
    
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
    
    def search_persoana_nume(self,key):
        persoana=Persoana("",key,"")
        return self.__repo_persoane.get_client_by_nume(persoana)
    
    def search_persoana_cnp(self,key):
        persoana=Persoana("","",key)
        return self.__repo_persoane.get_client_by_cnp(persoana)
    def search_persoana_nume1(self,key):
        persoana=Persoana("",key,"")
        return self.__repo_persoane.get_only_client_by_nume(persoana)
    

    
class ServiceInchiriere:
    
    def __init__(self,repo_inchiriere,valid_inchiriere,repo_carti,repo_persoane):
        
        self.__repo_inchiriere=repo_inchiriere
        self.__valid_inchiriere=valid_inchiriere
        self.__repo_carti=repo_carti
        self.__repo_persoane=repo_persoane
        
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
            carte=inchiriere.get_carte().get_titlu()
            client=inchiriere.get_client().get_nume()
           
            inchiriere_dto=InchiriereDTO(id_inchiriere,carte,client)
            inchirieri_dtos.append(inchiriere_dto)
        return inchirieri_dtos
         
    def remove_inchirieri_by_id_carte(self,id_carte):
        #pass
        inchirieri=self.__repo_inchiriere.get_all()
        
        for inchiriere in inchirieri:
            if inchiriere.get_carte().get_id()==id_carte:
                 self.__repo_inchiriere.remove(inchiriere)
           #

       
    def remove_persoana_by_id(self,id_persoana):
        inchirieri=self.__repo_inchiriere.get_all()
        for inchiriere in inchirieri:
            if inchiriere.get_client().get_id1()==id_persoana:
                self.__repo_inchiriere.remove(inchiriere)        
        
    def remove_inchiriere_by_id(self,key):
        inchiriere=Inchiriere(key,"","","")
        self.__repo_inchiriere.remove(inchiriere)           
  
    def cele_mai_inchiriate(self):
        carte=[]
        inchi={}
        rez=[]
        inchirieri=self.__repo_inchiriere.get_all()
        for i in inchirieri:
            car=i.get_carte().get_id()
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
            
    def clientii(self):
        inchi={}
        inchirieri=self.__repo_inchiriere.get_all()
        for i in inchirieri:
            cl=i.get_client().get_nume()
            if   cl in inchi:
                inchi[cl]+=1
            else :
                inchi[cl]=1
                
        return inchi
    
    def autorii(self):
        inchi={}
        import operator
        rez=[]
        inchirieri=self.__repo_inchiriere.get_all()
        for i in inchirieri:
            aut=i.get_carte().get_autor()
            if aut in inchi:
                inchi[aut]+=1
            else:
                inchi[aut]=1
        
        rez=sorted(inchi.items(), key=operator.itemgetter(1),reverse=True)

        return rez
            

