("délais de livraison")
qp= int(input("veuillez saisir la quantité produi"))
va= input(("veuillez écrire le mode de liversion normale/ rapide"))
print("va vaut:",  va )

va="rapide"
if qp<50: 
    d="2 jours"
    
elif 50 <qp <100: 
    d= "3 jours"
else :
    va= "5jours"
va="normale"
if qp<50:
    d=4
elif qp<100:
    va=5
else:
    d=7
print ("pour la quantité produitt: qp vaut:",qp)
print("pour le mode de liversion est: ", d)




