# Verwende das offizielle Python-Image als Basis
FROM python:3.9-slim

# Arbeitsverzeichnis im Container festlegen
WORKDIR /app

# Kopiere die Python-Abhängigkeiten und installiere sie
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Rest des Anwendungs-Codes
COPY . .

# Starte den Python-Server beim Start des Containers
CMD ["python", "./main.py"]