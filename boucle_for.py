#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

chaine = "Bonjour les ZER0S"
for lettre in chaine:
    if lettre in "AEIOUYaeiouy": # lettre est une voyelle
        print(lettre)
    else: # lettre est une consonne... ou plus exactement, lettre n'est pas une voyelle
        print("*")