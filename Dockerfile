# Utilise une image Python légère
FROM python:3.11-slim

# Définit le répertoire de travail
WORKDIR /app

# Copie les fichiers de dépendances
COPY requirements.txt .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie le reste du code
COPY . .

# Définit la variable d'environnement pour l'API Mistral
# (À passer via docker run -e ou docker-compose)
ENV MISTRAL_API_KEY=""

# Commande par défaut : lance l'agent en mode interactif
CMD ["python", "main.py"]