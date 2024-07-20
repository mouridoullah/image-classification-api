FROM python:3.8-slim

WORKDIR /app

COPY app/ /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exposer le port pour Flask
EXPOSE 5000

# Définir la commande de lancement
CMD ["python", "main.py"]
