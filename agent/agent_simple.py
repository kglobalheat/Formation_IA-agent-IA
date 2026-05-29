import os
import re
from dataclasses import dataclass
from typing import Dict, Callable, Optional
from mistralai import Mistral
from .memoire import MemoireAgent
from .outils.calculatrice import calculer
from .outils.gestion_fichiers import sauvegarder_fichier, lire_fichier

@dataclass
class Outil:
    """Représente un outil que l'agent peut utiliser."""
    nom: str
    description: str
    fonction: Callable

class AgentSimple:
    """Agent IA autonome de base avec Mistral."""

    def __init__(self, api_key: str, model: str = "mistral-tiny"):
        self.client = Mistral(api_key=api_key)
        self.model = model
        self.memoire = MemoireAgent()
        self.histoire: list[dict] = []
        self.outils: Dict[str, Outil] = {
            "calculatrice": Outil(
                nom="calculatrice",
                description="Effectue des calculs mathématiques simples.",
                fonction=calculer
            ),
            "sauvegarder_fichier": Outil(
                nom="sauvegarder_fichier",
                description="Sauvegarde du texte dans un fichier.",
                fonction=sauvegarder_fichier
            ),
            "lire_fichier": Outil(
                nom="lire_fichier",
                description="Lit le contenu d'un fichier.",
                fonction=lire_fichier
            )
        }

    def penser(self, prompt: str) -> str:
        """Utilise Mistral pour raisonner. On lui ordonne d'utiliser des balises pour les actions."""
        messages = [
            {
                "role": "system",
                "content": (
                    "Tu es un agent IA autonome. Ne fais JAMAIS de calculs complexes toi-même.\n"
                    "Pour utiliser un outil, écris : ACTION: nom_outil(argument)\n"
                    "Outils disponibles : calculer, sauvegarder_fichier, lire_fichier.\n"
                    "Exemple 1 : ACTION: calculer(125 * 8)\n"
                    "Exemple 2 : ACTION: sauvegarder_fichier(nom_fichier=\"test.txt\", contenu=\"Bonjour\")\n"
                    "Si la tâche est finie, commence par 'RÉPONSE FINALE :'."
                )
            },
            *self.histoire,
            {"role": "user", "content": prompt}
        ]
        response = self.client.chat.complete(
            model=self.model,
            messages=messages,
            temperature=0.7
        )
        reponse = response.choices[0].message.content
        self.histoire.append({"role": "assistant", "content": reponse})
        self.memoire.ajouter({"prompt": prompt, "reponse": reponse})
        return reponse

    def utiliser_outil(self, nom_outil: str, *args) -> str:
        """Exécute un outil et retourne le résultat."""
        if nom_outil in self.outils:
            return self.outils[nom_outil].fonction(*args)
        return f"Outil {nom_outil} non trouvé."

    def executer_tache(self, tache: str, max_iterations: int = 5) -> str:
        """Exécute une tâche en itérant entre réflexion et action."""
        self.histoire.append({"role": "user", "content": tache})
        contexte = self.memoire.recuperer_contexte()

        for iteration in range(max_iterations):
            # 1. Réflexion
            reflexion = self.penser(f"Contexte : {contexte}\nTâche : {tache}\nQue faire ensuite ?")
            print(f"[Itération {iteration + 1}] Réflexion : {reflexion}")

            # 2. Vérification de fin
            if self._est_termine(reflexion):
                return reflexion

            # 3. Extraction de l'action (simplifiée)
            action, argument = self._extraire_action_et_argument(reflexion)
            if action:
                resultat = ""
                if action == "calculer":
                    # Nettoyage spécifique pour la calculatrice
                    expr = argument.replace('×', '*').replace('x', '*')
                    resultat = self.utiliser_outil("calculatrice", expr)
                elif action == "sauvegarder_fichier":
                    # Extraction intelligente du nom et du contenu
                    nom_match = re.search(r'nom_fichier=["\'](.*?)["\']', argument)
                    cont_match = re.search(r'contenu=["\'](.*?)["\']', argument)
                    
                    nom = nom_match.group(1) if nom_match else "resultat.txt"
                    contenu = cont_match.group(1) if cont_match else argument
                    resultat = self.utiliser_outil("sauvegarder_fichier", nom, contenu)
                elif action == "lire_fichier":
                    # Extraction intelligente du nom de fichier
                    nom_match = re.search(r'nom_fichier=["\'](.*?)["\']', argument)
                    nom = nom_match.group(1) if nom_match else argument.strip().strip('"\'')
                    resultat = self.utiliser_outil("lire_fichier", nom or "resultat.txt")

                print(f"[Action] {action}({argument}) → {resultat}")
                contexte.append({"action": action, "resultat": resultat})
                self.histoire.append({"role": "assistant", "content": f"Résultat de l'outil : {resultat}"})

        return "Tâche non terminée dans la limite d'itérations."

    def _est_termine(self, texte: str) -> bool:
        """Vérifie si la tâche est terminée."""
        indicateurs = ["terminé", "fini", "réponse finale"]
        return any(ind in texte.lower() for ind in indicateurs)

    def _extraire_action_et_argument(self, texte: str):
        """Extrait proprement l'action et son argument via regex."""
        match = re.search(r"ACTION:\s*(\w+)\((.*)\)", texte)
        if match:
            return match.group(1), match.group(2).strip()
        return None, None