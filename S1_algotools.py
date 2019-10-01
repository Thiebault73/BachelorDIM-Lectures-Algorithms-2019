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
    if not(isinstance(tab,list)):
        raise ValueError('max_value, expected a list as input')
    valeurMax=tab[0]
    indice=0
    for i in range(len(tab)):
        if tab[i] > valeurMax :
            valeurMax = tab[i]
            indice = i
    return valeurMax, indice
# Test de la fonction
tab = [1,5,9,1,6,7]
res = max_value(tab)
print('Resultat =', res)


# Fonction  revers_table
def reverse_table(tab):
    if not(isinstance(tab, list)):
        raise ValueError('average_above_zero, expected a list as input')
    return print(list(reversed(tab)))
# Test de la fonction
tab = [1,2,3,4,5]
test = reverse_table(tab)

def reverse_table2(tab):
    if not(isinstance(tab,list)):
        raise ValueError('reverse_table2, expected a list as input')
    buffer = len(tab)
    taille = int(buffer/2)
    for id in range(taille):
        oppid = buffer - id - 1
        temp = tab[id]
        tab[id] = tab[oppid]
        tab[oppid] = temp
    return(tab)
    
#Test de la fonction
tab = [1,2,3,4,5]
inv = reverse_table2(tab)


# Fonction MATRICE
import numpy as np

''' Création de matrice avec que des 0 '''
matrix = np.zeros((10,10), dtype=np.int32)

''' Remplissage de la matrice avec des 1 aux coordonnées  ci-dessous '''
matrix[3:6, 4:8]=np.ones((3,4), dtype=np.int32)

''' Bibliothèque pour les images '''
import cv2

''' Importation img '''
img = cv2.imread('truc.png',0)

''' Affichage d'img '''
cv2.imshow('read image', img)
cv2.waitKey()
ptD =0
ptB = 0
ptH = 0
ptG = matrix.shape[1]
for idrow in range(matrix.shape[0]):
    for idcol in range(matrix.shape[1]):
        pixVal=[idrow, idcol]
        
        if matrix[idrow, idcol] == 1:
            
           if ptB < idrow :
              positionB=[idrow, idcol]
              
           if ptH == 0:
               positionH=[idrow, idcol]
               ptH = 1
               
           if ptD < idcol:
               ptD=idcol
               positionD=[idrow, idcol]
               
           if ptG > idcol:
               ptG=idcol
               positionG=[idrow, idcol]
               
print(positionH)
print(positionB)
print(positionD)          
print(positionG)       

# Fonction random_full_sparse(table: tableau numpy, K: int)
import numpy as np
def random_full_sparse (tab, K):
    tab[5,5]:np
    print(tab)
    
    

    
    
