def algo_cesar(mes, dec, sens):
    chiffres_cesar = ""
    mini = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    maji = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    

    for i in mes:
        if i.isupper():
            index = maji.index(i)
            if sens == "normal":
                nouvelle_index = (index + dec)
            elif sens == "inverse":
                nouvelle_index = (index - dec) 
            chiffres_cesar = chiffre_cesar+maji[nouvelle_index]
        
        elif i.islower():
            index = mini.index(i)
            if sens == "normal":
                nouvelle_index = (index + dec)
            elif sens == "inverse":
                nouvelle_index = (index - dec) 
            chiffres_cesar =chiffres_cesar+ mini[nouvelle_index]
        
        else:
            chiffres_cesar = chiffres_cesar+i
    
    return chiffres_cesar

mes = input("Veuillez saisir le message : ")
dec = int(input("Saisissez la valeur de décalage : "))
sens = input("Saisissez le sens de décalage (normal ou inverse) : ")

chiffres_cesar = algo_cesar(mes, dec, sens)
print("chiffres_cesar: ", chiffres_cesar)
