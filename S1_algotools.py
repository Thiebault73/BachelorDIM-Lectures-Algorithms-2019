# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:17:05 2019

@author: bebert
"""

# Fonction qui aditionne les nombres d'un tableau puis compte le nombre
# d'indice de celui-ci, avant de diviser le nombre max optenu par le nombre
# total d'indice obtenus.

def average_above_zero(tab):
    if not(isinstance(tab, list)):
        raise ValueError('average_above_zero, expected a list as input')
    somme = 0
    n = 0
    for i in range(len(tab)):
        if tab[i] > 0 :
            somme = somme + tab[i]
            n = n + 1
    if n == 0:
        return print ('Division par 0 impossible')
    moyenne = (somme / n)
    return moyenne
# Test de la fonction
tab = [1,2,3,4]
somme = average_above_zero(tab)
print('resultat =', somme)

# Fonction qui récupère le nombre max d'une liste et son indice.
def max_value(tab):
    valeurMax = 0
    for i in range(len(tab)):
        valeurMax = tab[i]
        if valeurMax == max(tab) :
            return valeurMax, i
# Test de la fonction
tab = [1,5,9,1,6,7]
res = max_value(tab)
print('Resultat =', res)


# Fonction  revers_table
def reverse_table(tab):
    print(list(reversed(tab)))
    return tab
# Test de la fonction
tab = [1,2,3,4,5]
test = reverse_table(tab)
