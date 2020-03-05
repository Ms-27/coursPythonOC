def table(nb, max=10): # On doit renseigner un entier et une valeur max (optionnellle), par défaut elle vaut 10
    
    # docstring, apparait avec la commande: help(table)
    """Fonction affichant la table de multiplication par nb
    de 1*nb à max*nb (max >= 0), par défaut max = 10"""
    i = 1
    while i <= max:
        print(i, "*", nb, "=", i*nb)
        i += 1

var = int(input("Saisir un chiffre: "))
table(var)