
class Sorts:
    
    
    def selection_sort(self,lista,key=lambda l,x:l[x][0],reversed=False):
        
        for i in range(0,len(lista)-1):
            for j in range(i+1,len(lista)):
#                  
                if reversed==False:
                    #if key(lista,i)>key(lista,j):
                    if key(lista,i)>key(lista,j):
                        lista[i], lista[j]=lista[j], lista[i]
                else:
                    if reversed==True:
                        if key(lista,i)<key(lista,j):
                            lista[i], lista[j]=lista[j], lista[i]
#                 
        return lista
    
    def selection_sort2(self,lista,key1=lambda l,x:l[x][1],key2=lambda l,x:l[x][0],reversed=False):
        
        for i in range(0,len(lista)-1):
            for j in range(i+1,len(lista)):
#                  
                if reversed==False:
                    if key1(lista,i)>key1(lista,j):
                        lista[i], lista[j]=lista[j], lista[i]
                    else:
                        if key1(lista,i)==key1(lista,j):
                            if key2(lista,i)>key2(lista,j):
                                lista[i], lista[j]=lista[j], lista[i]
                else:
                    if key1(lista,i)<key1(lista,j):
                        lista[i], lista[j]=lista[j], lista[i]
                    else:
                        if key1(lista,i)==key1(lista,j):
                            if key2(lista,i)>key2(lista,j):
                                lista[i], lista[j]=lista[j], lista[i]
                    
                
        return lista
        
#         
    def shak_sort(self,lista,key=lambda l,x:l[x][0],reversed=False):
        
        def schimba(a, b):
            lista[a],lista[b]= lista[b],lista[a]
 
        d=len(lista) - 1
        s=0
 
        ok = False
        while (not ok and d - s > 1):
            ok = True
            for j in range(s, d):
                if reversed==False:
                    if key(lista,j + 1) < key(lista,j):
                        schimba(j + 1, j)
                        ok = False
                else:
                    if key(lista,j + 1) > key(lista,j):
                        schimba(j + 1, j)
                        ok = False
                    
            d = d-1
 
            for j in range(d, s, -1):
                if reversed==False:
                    if key(lista,j - 1) > key(lista,j):
                        schimba(j - 1, j)
                        ok=False
                    
                else:
                    if key(lista,j - 1) < key(lista,j):
                        schimba(j - 1, j)
                        ok=False
                    
            s= s+1

        return lista

    
    