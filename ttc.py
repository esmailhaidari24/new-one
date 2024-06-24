
print("cacul tva et ttc ")
ht=(float(input("veuillez saisir le montant HT")))
print("le montant HT est:",ht )
taux= float(input("veuillez saisir le montant de tva"))
print("le montant de tva est:", taux)

tva =ht*(taux/100)
print("tva vaut:", tva)
ttc=ht+tva
print("ttc", ttc)

