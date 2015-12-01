#!/usr/bin/env python
#encoding=utf-8
import numpy as np
from tp2function import *

### Données ###
A = np.array([14,10,12,11,10,9]).reshape(3,2) # On créer la matrice
print("Matrice A :")
print(A) # On l'affiche
print("Nombre de colones de A:")
nbColones = A.shape[1]
print(nbColones) # Nombre de ligne et de colones de A
canoniqueR3 = np.array([1,0,0,0,1,0,0,0,1]).reshape(3,3) # On créer la base canonique de R³
print("Base canonique de R³")
print(canoniqueR3)
canoniqueR2 = np.array([1,0,0,1]).reshape(2,2) # On créer la base canonique de R²
print("Base canonique de R²")
print(canoniqueR2)

## Matrice de corrélation ###
for j in xrange(0,nbColones):
 	moy = moyenne(A[:,j])
 	matMoy = moy*np.ones(nbColones,dtype=np.int) # Calcul de la moyenne
 	print("Moyenne colonne")
 	print(matMoy)
	ecartT = ecartType(A[:,j],moy)
	print("Ecart type colone")
	print(ecartT)
	print("Caractere centre")
	caratereC = caractereCentre(A[:,j],moy)
	print(caratereC)
	caratereCR = caractereCentreReduit(caratereC,ecartT)
	print("Caratere centre reduit")
	print(caratereCR)