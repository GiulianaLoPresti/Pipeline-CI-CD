Dal sito Airflow:
https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

#### Terminale
cd Orchestration

### Sez Fetching docker-compose.yaml
#### Terminale
Copia link curl ecc. nel terminale
Scarica il file docker-compose dentro la cartella Orchestration


### Sez Initializing Environment
#### Creiamo le 4 cartelle: dags, logs, config, plugins e env   DENTRO ORCHESTRATION 
In env si inserisce AIRFLOW=UID

#### Terminale
mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env

Inseriamo in logs il file .gitignore e gli scriviamo "*  !.gitignore" e salviamo

Facciamo il commit e lo chiamiamo "airflow configurations"

Dalla documentazione, inizializziamo i database
#### Terminale
docker compose up airflow-init
Docker compose scarica le immagini, redis e postgres sono dei db 

### Se non funziona, per eliminre quello che abbiamo fatto e ricominciare da capo
Cleaning-up the environment

### Se tutto funziona:
docker compose up
