import os
from typing import Optional

BASE_PATH = "./data"

def sauvegarder_fichier(nom_fichier: str, contenu: str) -> str:
    """Sauvegarde du contenu dans un fichier."""
    os.makedirs(BASE_PATH, exist_ok=True)
    chemin = os.path.join(BASE_PATH, nom_fichier)
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(contenu)
    return f"Fichier '{nom_fichier}' sauvegardé avec succès dans le dossier '{BASE_PATH}' de votre projet."

def lire_fichier(nom_fichier: str) -> str:
    """Lit le contenu d'un fichier."""
    chemin = os.path.join(BASE_PATH, nom_fichier)
    if os.path.exists(chemin):
        with open(chemin, "r", encoding="utf-8") as f:
            return f.read()
    return f"Fichier {nom_fichier} introuvable."