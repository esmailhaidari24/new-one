def calcul_tarif(pu):
    if pu < 20:
        pu = pu * 1.1
    elif pu < 50:
        pu = pu * 1.075
    elif pu < 100:
        pu = pu * 1.05
    else:
        pu = pu * 1.025
    return round(pu, 2)

