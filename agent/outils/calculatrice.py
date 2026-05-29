from typing import Callable

def calculer(expression: str) -> str:
    """Effectue un calcul mathématique simple."""
    try:
        # Sécurité : désactive les builtins pour éviter les commandes dangereuses
        return str(eval(expression, {"__builtins__": None}, {}))
    except Exception as e:
        return f"Erreur de calcul : {str(e)}"