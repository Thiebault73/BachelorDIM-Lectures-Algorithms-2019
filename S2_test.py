# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 17:02:59 2019

@author: bebert
"""

import pytest
import S1_algotools as S1
import numpy as np

def inc_(x):
    return x+1

def test_inc():
    assert inc_(3)==4
    

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1/0
        
        
#################################### 
## Tests unitaires pour l'exercice 1
####################################
        
## On teste si la moyenne est bien réalisée
def test_ex1_1():
    tab = [1,2,3,4]
    assert S1.average_above_zero(tab) == 2.5
    
## On teste les nombres négatifs
def test_ex1_2():
    tab = [-1,-2,-3,-4]
    with pytest.raises(ZeroDivisionError):    
        assert S1.average_above_zero(tab)

## On teste la fonction en ne lui passant pas de liste
def test_ex1_3():
   with pytest.raises(ValueError):
       S1.average_above_zero(["YO", "31"])
       
     
#####################################
## Tests unitaires pour l'exercice 2   
#####################################
       
## On teste si la fonction fonctionne correctement
def test_ex2_1():
    tab=[1,2,3,89,5,6,7]
    assert S1.max_value(tab)==(89,3)
    
## On teste la fonction en ne lui passant pas de liste
def test_ex2_2():
    with pytest.raises(TypeError):
        S1.max_value("YO")
        
        
####################################
## Tests unitaires pour l'exercice 3
####################################
    
## On teste si la fonction fonctionne correctement
def test_ex3_1():
    tab=[1,2,3,4,5]
    assert S1.reverse_table2(tab) == [5,4,3,2,1]
    
## On teste s'il ne s'agit pas d'une liste
def test_ex3_2():
    with pytest.raises(TypeError):
        S1.reverse_table2("YO")
    

####################################
## Tests unitaire pour l'exercice 4
####################################
        
## On teste  la fonction en lui passant une chaîne de caractère au lieu d'une 
## liste
def test_ex4_1():
     with pytest.raises(TypeError):
        S1.roi_bbox("YO")
        
###################################
## Tests unitaire pour l'exercice 5
###################################

## On test le bon fonctionnement de la fonction
def test_ex5_1():
    tab = np.ones((10,10), dtype=np.chararray)
    tab *= ' '
    tabF = S1.random_full_sparse(tab,3)
    assert len(np.argwhere(tabF=='X')) == 3  
    
## On passe une chaîne de caractère en paramètre
def test_ex5_2():
    tab = np.array([1,2,3,4])
    with pytest.raises(TypeError):
        S1.random_full_sparse(tab,"YO")
       
       
       
    