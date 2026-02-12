# Si crea semplicemente facendo un nuovo file e chiamandolo dockerfile

# Uso un'immagine di base di Python
FROM python:3.10-slim 

# Copiamo il contenuto della directory
#./ inica la cartella dove si trova il docker file, poi specifichiamo meglio il percorso
COPY ./workspaces/Pipeline-CI-CD/CD/app /app

# copiamo tutto quello che sta il CD nella cartella app del docker container

# Settiamo la work dir, dove lavoreremo
WORKDIR /app
# Comando per verificare che stia funzionando, quando andremo a vedere i log, cioè vedremo la lista dei file nella cartella app
RUN ls

# Eseguiamo il file app.py
CMD["python","app.py"]
