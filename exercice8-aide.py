##########################################################################
##########################################################################
# Exercice 8 : avec Numpy
##########################################################################
##########################################################################

##############
# question 1
##############

# comme X, Y, T, sont des tableaux, on peut faire des calculs naturels à partir d'eux
Ep = ..... # à compléter
Ec = ..... # à compléter
E = ..... # à compléter



##############
# question 2
##############

# construction de Ep en fonction du temps
plt.plot( , , "b-",label="énergie potentielle")

# construction de Ec en fonction du temps
..... # à compléter

# construction de E en fonction du temps
..... # à compléter

# un titre au graphe
..... # à compléter

# affichage des valeurs des 4 tableaux T, Ep, Ec, E
for i in range(....) : # à compléter : que doit parcourir i ? 
    print("temps : ",T[i], "   Ep : ",Ep[i], "   Ec : ",Ec[i], "   E : ", E[i])


plt.legend()
plt.show()


##############
# question 3
##############
# initialisation de la liste Xarrondie
....... # à compléter

# implémentation de Xarrondie
for i in X : # pour chaque élément de X
    ...... # à compléter : on arrondit i au 1er chiffre après la virgule
    ...... # à compléter : on l'ajoute à la liste Xarrondie

# On affiche X et Xarrondie
# à compléter

