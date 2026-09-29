import sys

sys.stdout.write("Ecris quelque chose: |")
# python prend ta phrase et la place dans un espace 
# de stockage temporaire en memoire appelé le buffer (le tempon)
sys.stdout.flush()
# Ordonnes à python: "vide  le buffer immédiatement et balance tout ce qu'il y a dedans sur l'ecran de l'utilisateur"
# sys.stdin.readline() lit une ligne tapée par l'utilisateur
user_input = sys.stdin.readline()
# petit detail : readline() garde souvent le saut de ligne (\n) à la fin

# donc on utilise .strip() pour le nettoyer proprement
user_input_propre = user_input.strip()
print(f"Tu as : {user_input_propre}")
