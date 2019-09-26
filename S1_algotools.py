# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:17:05 2019

@author: bebert
"""

# Fonction qui aditionne les nombres d'un tableau puis compte le nombre
# d'indice de celui-ci, avant de diviser le nombre max optenu par le nombre
# total d'indice obtenus.

def average_above_zero(table:list):
    somme = 0
    n = 0
    for i in range(len(table)):
        if table[i] > 0 :
            somme = somme + tab[i]
            n = n + 1
    if n == 0:
        return print ('Division par 0 impossible')
    moyenne = (somme / n)
    return moyenne
## Test de la fonction
tab = [1,2,3,4]
somme = average_above_zero(tab)
print('resultat =', somme)

