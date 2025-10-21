# Exemples d'utilisation de la fonction print en Python

print("Hello, World!")                            # affichage simple

# plusieurs arguments (séparés par un espace par défaut)
print("Bonjour", "le", "monde!")

# séparateur personnalisé
print("2025", "10", "21", sep="-")

# modifier le caractère de fin (par défaut '\n')
print("Ligne sans saut de ligne...", end="")
print(" <-- suite sur la même ligne")

# f-strings (formatage moderne, Python 3.6+)
name = "Alice"
age = 30
print(f"{name} a {age} ans.")

# afficher la représentation officielle d'un objet
obj = {"a": 1}
print("repr:", repr(obj))

import sys
# écrire sur stderr instead of stdout
print("Erreur simulée", file=sys.stderr)

# flush=True force l'écriture immédiate (utile pour les logs)
print("Flush example", flush=True)