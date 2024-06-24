def pal(mot):
    return mot==mot[::-1]
     
# algorithme principal

mot= str(input("veuillez saisir un mot"))
if pal(mot):
    print(mot, "est un palindrome.")
else:
    print(mot, "n'est pas un palindrome.")

