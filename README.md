# Agent IA Autonome avec Mistral et Docker

Ce projet est une base d'étude pour comprendre le fonctionnement des **Agents IA**. Il utilise un LLM (**Mistral AI**) capable d'utiliser des outils Python pour résoudre des tâches complexes.

---

## 📌 Prérequis

*   **Docker & Docker Compose** installés.
*   Une **clé API Mistral** (disponible sur [console.mistral.ai](https://console.mistral.ai/home) ).

---

## 🚀 Installation et Lancement

1. **Cloner le projet** :
   ```bash
   git clone <url-du-repo>
   cd agent-IA
   ```

2. **Configurer l'environnement** :
   Crée un fichier `.env` à la racine (ou complète celui existant) avec ta clé :
   ```env
    # Clé API Mistral (à obtenir sur console.mistral.ai)
    MISTRAL_API_KEY=votre_cle_ici

    # Paramètres optionnels
    MODEL=mistral-tiny  # ou "mistral-small" pour plus de puissance
    MAX_ITERATIONS=5
   ```

1. **Lancer l'agent (Mode Interactif)** :
   C'est la commande recommandée pour pouvoir discuter avec l'agent :
   ```bash
   docker-compose run agent-ia
   ```

2. **Mise à jour après modification du code** :
   Si vous modifiez les outils ou la logique, reconstruisez l'image :
    ```bash
    docker-compose up --build
    ```

---
## 🧪 Exemples d'utilisation

Une fois le conteneur lancé, tu peux tester l'agent avec des tâches comme :
- `Calcule 125 * 8`
- `Calcule 126*9-3`
- `Calcule 15 + 27 et dis-moi si le résultat est pair.`
- `Sauvegarde la phrase 'Bonjour tout le monde' dans un fichier nommé test.txt`
- `Lis le contenu du fichier test.txt`

---
## 🔧 Personnalisation

- **Ajouter un outil** :
  Crée un nouveau fichier dans `agent/outils/` et ajoute-le dans `agent_simple.py`.

- **Changer le modèle** :
  Modifie la variable `MODEL` dans `.env` (`mistral-tiny` ou `mistral-small`).

- **Tout comprendre** :
  Pour comprendre comment l'IA "réfléchit" et utilise les outils, consultez le fichier : 👉 CONCEPTS.md, vous y trouverez aussi quelques exercices!

---
## 📂 Structure du projet
```
agent-IA/
├── CONCEPTS.md
├── Dockerfile
├── README.md
├── agent/
│   ├── __init__.py
│   ├── agent_simple.py
│   ├── memoire.py
│   └── outils/
│       ├── calculatrice.py
│       └── gestion_fichiers.py
├── data/
├── docker-compose.yml
├── main.py
└── requirements.txt
```

---
## 🤝 Contribuer
Ce projet est conçu pour être étendu. N'hésite pas à ajouter des outils ou améliorer l'agent !
```
