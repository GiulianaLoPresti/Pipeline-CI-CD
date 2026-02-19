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