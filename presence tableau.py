
tab= [1,2,4,5,6,7,8,9,23,24]

print("tableau", tab)

E= int(input("veuillez saisir un entier"))

n=0

for i in range(0,10,1):
   if i==E:
       n=n+1
if n>0:
        print(" entier est présente :", n)
else:
    ("non")







en pseduo longage

Algorithme: présence de entier 
type= entier

début

tab<--[1, 2, 4, 5, 6, 7, 8, 9, 23, 24]

Afficher ()"tableau", tab)

n = 0

E = saisir("veuillez saisir un entier")

Pour chaque i de 0 à 9 (inclus)
    Si tab[i] == E alors
        n = n + 1
Fin Pour

Si n > 0 alors
    Afficher "entier est présent :", n
Sinon
    Afficher "rien"

fin