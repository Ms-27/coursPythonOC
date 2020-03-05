#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

# Demande de saisir une année
annee = input("Saisissez une année: ")
annee = int(annee)
# Affiche l'année saisie
print(annee)

# Ecriture de la condition
if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("Année bisextile")
else:
    print("Année non bissextile") 