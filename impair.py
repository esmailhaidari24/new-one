


tab= [1,2,4,5,6,7,8,9,23,24]
print(tab)
for i in range(0,10,1):
    print(tab [i])
if tab[i] % 2 == 0:
    print("tab est paire")
else:
    ("tab est imapair")
    
    
    
    #la douxième possibilité
    
    
tab= [1,2,4,5,6,7,8,9,23,24]
print("tab")
while True:
    for i in range(0,10,1):
        print(i)
        
        if (tab[i]) %2==0:
            print("tab est pair")
        else:
        
         print("tab est impair")
    break



en pseduo longage 


Algorithme: paire/impair
type: entier

début 

tap<-- [1, 2, 4, 5, 6, 7, 8, 9, 23, 24]
afficher(tab)

pour chaque élément i de 0 à 9 faire
    afficher(tab[i])
    
    si tab[i] modulo 2 est égal à 0 alors
        afficher("tab est paire")
    sinon
        afficher("tab est impair")
    fin si
fin pour

fin
