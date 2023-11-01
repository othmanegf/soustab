def sousTableau(t,n, m):        
    sous_tab = t[n:m]
    return sous_tab
t=[]
for i in range(0,9):
     print("entrer l'element",i+1,"du tableau:")
     t.append(input())
n=int(input("indice de debut:"))
m=int(input("indice de fin:"))
sous_tab =sousTableau(t,n, m)
print("le sous tableau d'index",n,",",m,"est:",sous_tab)