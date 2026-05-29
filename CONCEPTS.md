# Concepts fondamentaux des Agents IA

Ce projet illustre comment transformer un modèle de langage (LLM) "passif" en un **Agent autonome**.

## 1. La boucle ReAct (Reason + Act)

L'agent ne répond pas directement. Il suit un cycle itératif :
1.  **Réflexion (Reason)** : L'IA analyse la demande et décide si elle a besoin d'un outil (ex: "Je dois faire un calcul").
2.  **Action** : Si besoin, l'IA émet une commande spéciale (ex: `ACTION: calculer(2+2)`).
3.  **Observation** : Le code Python intercepte cette commande, l'exécute, et redonne le résultat à l'IA.
4.  **Finalisation** : Une fois qu'elle a toutes les informations, l'IA produit la réponse finale.

## 2. Le "System Prompt" : Le rôle de l'agent

Dans `agent_simple.py`, nous définissons des instructions strictes qui ne sont pas visibles par l'utilisateur mais qui dictent le comportement de l'IA. C'est ici qu'on lui interdit de calculer elle-même et qu'on lui apprend la syntaxe des outils.

## 3. Tool Use (Utilisation d'outils)

Un LLM est excellent pour le langage mais mauvais pour les faits précis (calculs, météo, base de données). 
*   **L'IA** : Est le "cerveau" qui décide quoi faire.
*   **Les outils (Python)** : Sont les "mains" qui exécutent les tâches de manière déterministe.

## 4. La Mémoire et le Contexte

L'IA n'a pas de mémoire innée entre deux questions. 
*   La **mémoire court terme** (dans `memoire.py`) réinjecte l'historique de la conversation actuelle dans chaque nouvelle question envoyée au modèle pour qu'il garde le fil de la discussion.

## 5. Pourquoi Docker ?

L'utilisation d'un agent capable d'exécuter du code (comme via `eval()` dans la calculatrice) présente des risques de sécurité. Docker permet de :
1.  **Isoler** l'exécution : l'agent ne peut pas abîmer votre ordinateur personnel.
2.  **Standardiser** : l'étudiant a exactement le même environnement que le professeur, peu importe son système d'exploitation.
3.  **Persister les données** : Le dossier `data/` de votre projet est monté dans le conteneur (`./data:/app/data`), ce qui signifie que les fichiers créés par l'agent (comme `test.txt`) sont directement accessibles sur votre machine hôte.


## Exercices

### Premiers exercices:
1.  **Modifier le Prompt** : Changez le ton de l'agent dans `agent_simple.py` (faites-en un robot sarcastique).
2.  **Créer un Outil** : Ajoutez un outil dans `agent/outils/` qui donne l'heure actuelle ou génère un nombre aléatoire.
3.  **Observer les logs** : Regardez dans le terminal comment l'IA hésite ou se corrige entre deux itérations.

### Exercices avancés:
1. **Rechercher sur le web** :Ajoutez un outil de recherche sur le web via DuckDuckGo (nécessite le package duckduckgo-search)
2. **Mémoire long terme** : Remplacez la mémoire en `deque` par une base PostgreSQL.