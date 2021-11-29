try:
    n = int(input("Saisissez le nombre de valeur du tableau"))
    tab = {}
    nb_negatif = int(0)
    nb_positif = int(0)

    for i in range(n):
        print("Valeur", i, "du tableau:")
        tab[i] = int(input())
        if tab[i] < 0:
            nb_negatif += 1
        else:
            nb_positif += 1
    print("Il y a ", nb_negatif, "nombre négatif")
    print("Il y a ", nb_positif, "nombre positif")
except ValueError:
    print("saisie non valide")


