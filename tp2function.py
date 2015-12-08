#!/usr/bin/env python
#encoding=utf-8

import numpy as np
from math import *

def moyenne(matrice):
	somme = 0
	for x in xrange(0,matrice.size):
		somme += matrice[x] # On fait la somme de toutes les valeurs
	return(somme/matrice.size)

def caractereCentre(matrice,moyenne):
	return(matrice-(moyenne*np.ones(matrice.shape[0],dtype=np.int))) # On soustrait la matrice Xj à une matrice de la moyenne

def ecartType(matrice,moyenne):
	somme=0
	for x in xrange(0,matrice.size):
		somme+=(matrice[x]-moyenne)**2 ## On somme toutes les valeurs en les soustrayant à la moyenne
	return (sqrt((1.0/matrice.size)*somme))

def caractereCentreReduit(caractereC,ecartype):
	return (caractereC/ecartype)# On divise le caractère reduit par l'ecartype pour obtenir le caractere centré reduit

def correlation(Z):
	Zt = Z.T
	n = Z.shape[0]
	return((1.0/n)*np.dot(Zt,Z))