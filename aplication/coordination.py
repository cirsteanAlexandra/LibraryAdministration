from validation.validators import ValidatorCarte,ValidatorPersoana,ValidatorInchiriere
from infrastructure.repositories import RepositoryCarte, FileRepositoryCarte, NouFileRepositoryCarte, \
    FileRepositroyPersoana, FileRepositoryInchiriere, RepositoryPersoana, RepositoryInchiriere
from business.services import ServiceCarte,ServicePersoana,ServiceInchiriere
from presention.cons import UI
from methods.sort import Sorts
class AppCoord(object):
    
    
    def __init__(self):
        pass
    

    def start(self):
        while True:
            metoda=input("adauga metoda de persistenta: ")
            if metoda=="f":
                repo_carti=FileRepositoryCarte("carti.txt")
                #repo_carti=NouFileRepositoryCarte("altt1.txt")
                repo_persoane=FileRepositroyPersoana("clienti.txt")
                repo_inchiriere=FileRepositoryInchiriere("inchi.txt")
            elif metoda=="memorie":
                repo_carti=RepositoryCarte()
                repo_persoane=RepositoryPersoana()
                repo_inchiriere=RepositoryInchiriere()
                
            else:
                print("metoda de persistenta invalida! ")
                continue
            #repo_inchiriere=RepositoryInchiriere()
            valid_carte=ValidatorCarte()
            valid_persoana=ValidatorPersoana()
            valid_inchiriere=ValidatorInchiriere()
            sort=Sorts()
            srv_carti=ServiceCarte(repo_carti,valid_carte)
            srv_persoane=ServicePersoana(repo_persoane,valid_persoana)
            srv_inchiriere=ServiceInchiriere(repo_inchiriere,valid_inchiriere,repo_carti,repo_persoane,sort)
            cons=UI(srv_carti,srv_persoane,srv_inchiriere)
            cons.run()
    
            
                


