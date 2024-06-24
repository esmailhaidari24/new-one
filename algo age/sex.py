sex= input("veuillez saisir le sex de l'habitant h/f ")
age= int(input("veuillez saisir l'age de l'habitant "))

if (sex== 'h' and  age >=20) or (sex=='f' and age >=18 and age<= 35):
    print('habitant est imposable ')
     
else:
    print(" l'habitant nest pasimposable ")