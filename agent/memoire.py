from collections import deque
from datetime import datetime
from typing import List, Dict

class MemoireAgent:
    """Gère la mémoire court terme et long terme de l'agent."""

    def __init__(self, max_court_terme: int = 10):
        self.court_terme = deque(maxlen=max_court_terme)
        self.long_terme = []

    def ajouter(self, experience: Dict) -> None:
        """Ajoute une expérience à la mémoire court terme."""
        self.court_terme.append({
            "timestamp": datetime.now().isoformat(),
            "contenu": experience
        })

    def recuperer_contexte(self, limite: int = 5) -> List[Dict]:
        """Récupère les dernières expériences."""
        return list(self.court_terme)[-limite:]

    def marquer_comme_important(self, index: int, raison: str) -> None:
        """Déplace une expérience vers la mémoire long terme."""
        if 0 <= index < len(self.court_terme):
            memoire = dict(self.court_terme[index])
            memoire["raison_importance"] = raison
            self.long_terme.append(memoire)