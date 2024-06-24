
tableau = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10]
for i in range(0, 5):
 v = tableau[i]
tableau[i] = tableau[10 - i - 1]
tableau[10 - i - 1] = v
print(tableau)
    
    

