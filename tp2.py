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
print("Nombre de lignes de A:")
nbLignes = A.shape[0]
print(nbColones) # Nombre de ligne et de colones de A
canoniqueR3 = np.array([1,0,0,0,1,0,0,0,1]).reshape(3,3) # On créer la base canonique de R³
print("Base canonique de R³")
print(canoniqueR3)
canoniqueR2 = np.array([1,0,0,1]).reshape(2,2) # On créer la base canonique de R²
print("Base canonique de R²")
print(canoniqueR2)

## Matrice de corrélation ###
Zt = np.array([]) # On créer une matrice pour stocker la matrice centré rédruit transposé
for j in xrange(0,nbColones):
 	moy = moyenne(A[:,j])
 	matMoy = moy*np.ones(nbColones,dtype=np.int) # Calcul de la moyenne
 	print("Moyenne colonne")
 	print(matMoy)
	ecartT = ecartType(A[:,j],moy)
	print("Ecart type colone")
	print(ecartT)
	print("Caractere centre")
	caractereC = caractereCentre(A[:,j],moy) # On calcul le cartère centré
	print(caractereC)
	caractereCR = caractereCentreReduit(caractereC,ecartT) # On calcul le caractère centré et réduit
	print("Caratere centre reduit")
	print(caractereCR)
	Zt = np.append(Zt,caractereCR,axis=0) # On insert le caractère colone dans la matrice général
Zt = Zt.reshape(nbColones,nbLignes) # On transforme en matrice
Z = Zt.T # On transpose pour obtenir la matrice Z
print("Matrice Z du caractère centré réduit")
print(Z)
R = correlation(Z)
print("R, matrice de corrélation de Z")
print(R)


## Mode propre ##
valPropreR = np.linalg.eig(R)[0] # Calcul des valeurs propres et des vecteurs propre. On récupère chaque valeur indépendement.
vecPropreR = np.linalg.eig(R)[1]
print("Valeurs propres de R")
print(valPropreR)
print("Vecteurs propres de R")
print(vecPropreR)

## Axes principaux ##
C = np.array([]) # C permet de stocker les coordonnées des individus dans la base des axes principaux de R
for x in xrange(0,nbLignes):
	C = np.append(C,np.dot(vecPropreR.T,Z[x,:]),axis=0)
C = C.reshape(nbLignes,nbColones)
print("Coordonnées des individus dans la base des axes principaux de R")
print(C)

## Composante principale ##
