
"""mp= input("entrez votre mot de passe:")
if mp==mp[::-1]:
    print("le mot de passe est palindrom")
else: 
    print("mot de passe n'est pas palindrome")"""
    
def verifi_carte(numero_cart):
    print("numero carte")    
tableau=[int(i) for i in str(numero_carte)]
print("contune du tableau avant le calcul:", tableau)
for i in range(0,16,2):
    tableau[i]*=2
    if tableau[i]>9:
        tableau<-9
print("contunu après le calcul")
total= sum(tableau)
print("total:", total)
return total % 10 == 0

carte_saisie=(input("veuillez mettre votre carte bancaire:"))
carte_valide =verifie_carte("carte saisie")

if carte_valide:
    print("carte est valide ")
else:
    print("carte non valide")

