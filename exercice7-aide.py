#######################################################
#######################################################
# Exercice 7
#######################################################
#######################################################

import matplotlib.pyplot as plt
import numpy as np
from math import radians, cos, sin

################
# question 1
################
...... # entrer m, g et k et leurs valeurs et alpha (en degrés)
alpha = ... # transformer alpha en radians
tau = ....# à compléter
v0 = .....#à compléter : entrer v0 au début


################
# question 2
################
.....#à compléter : entrer t au début
.....# on entre t à la fin
.....# choisissez-vous un pas de temps
T = .....#à compléter :  construire l'intervalle de temps d'étude


################
# question 3
################
X = v0*cos(alpha)*tau*(1-np.exp(-(T/tau)))
Y = .....# à compléter
VX = .....# à compléter
VY = .....# à compléter


################
# question 4
################
plt.plot() # à compléter

plt.legend()
plt.show()
