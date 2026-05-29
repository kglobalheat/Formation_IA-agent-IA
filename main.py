import os
import sys
from agent.agent_simple import AgentSimple

def main():
    api_key = os.getenv('MISTRAL_API_KEY')
    if not api_key:
        print("Error: MISTRAL_API_KEY environment variable is not set.")
        sys.exit(1)

    agent = AgentSimple(api_key)
    print("--- Agent IA Connecté (Tapez 'quitter' pour sortir) ---")

    while True:
        try:
            tache = input("\nAgent IA prêt ! Tapez une tâche : ")
            
            if tache.lower() in ['quitter', 'exit', 'quit']:
                print("Au revoir !")
                break
                
            if tache.strip():
                resultat = agent.executer_tache(tache)
                print(f"\n[Résultat Final] : {resultat}")
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == "__main__":
    main()