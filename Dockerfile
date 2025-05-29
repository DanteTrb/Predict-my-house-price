# Usa un'immagine base leggera con Python
FROM python:3.11-slim

# Imposta la cartella di lavoro
WORKDIR /app

# Copia i file del progetto dentro il container
COPY . /app

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Espone la porta per il server Flask
EXPOSE 5000

# Avvia l'app Flask
CMD ["python", "-m", "app.api"]