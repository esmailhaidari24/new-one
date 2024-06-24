

miniute= float(input("veuillez saisir votre consomation habituelles par minuite"))

offre_1= 10+0.05 *miniute
offre_2= 20+0.02 *miniute

if offre_1<offre_2:
    print("offre_1 est plus avantagese")
else:
    print("offre_2 est plus avantagese")

