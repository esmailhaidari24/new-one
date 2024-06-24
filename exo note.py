

tab= [1,2,4,5,6,7,8,9,23,24]
print(tab)

mini_v = tab[0]
maxi_v = tab[0]

for i in range(1,10,1):
    if mini_v<tab[i]:
        mini=[i]
    if maxi_v>tab[i]:
        tab[i]=maxi_v
        
    print("la valeur le plus petit est", mini)
    print("la valeur le plus grand est", )
    
    
        
en pseduo longage 
    
Algorithme: le plus petit/grand
    
type: entier

début 

variable: mini_v,maxi_v

poir chaque élément i de 0 à 9 faire
    afficher(tab[i])
    
    si tab[i] modulo 2 est égal à 0 alors
        afficher("tab est paire")
    sinon
        afficher("tab est impair")
    fin si
fin pour

fin 