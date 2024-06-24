va=int(input("veuillez saisir le premier entier:"))
vb=int(input("veuillez saisir le second entier"))
vc=int(input("veuillez saisir le troisème entier"))
somme=(va+vb+vc)
print("somme vaut:", somme)
moyen=(somme/3)
print("moyen vaut:",moyen)

if va>vb and vc:
    print("va est le plus grand")
    
elif vb>vc:
        print("vb est le plus petit")
else:
    print("vc est le plus grand")
    
if va<vb and vc:
    print("va est le plus petit")
elif vb<va and vc:
    print("vb est le plus petit")
else:
    print("vc est le plus petit")
    

