#!/bin/python

myListe = [5, 7, 1, 9, 6, 4]
print("Liste initiale :")
print(myListe)

input()

# Exercice 1

i1 = 0
i2 = 5

aux = myListe[i1]
myListe[i1] = myListe[i2]
myListe[i2] = aux

print("Exercice 1:")
print(myListe)

input()

# Exercice 2

for i in range(len(myListe)-1):
    if myListe[i] > myListe[i+1]:
        aux = myListe[i]
        myListe[i] = myListe[i+1]
        myListe[i+1] = aux

print("Exercice 2:")
print(myListe)

input()

# Exercice 3

for i in range(len(myListe)):
    for j in range(len(myListe)-1):
        if myListe[j] > myListe[j+1]:
            aux = myListe[j]
            myListe[j] = myListe[j+1]
            myListe[j+1] = aux


print("Exercice 3:")
print(myListe)


input()

print("Exercice 4:")
print("Cet algorithme est tres lent car\
        il y a deux boucles imbriquees.\
        La complexite augmente donc avec la\
        taille de la liste et est logarithmique. ")
