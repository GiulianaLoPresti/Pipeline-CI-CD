"""
my first dag for airflow
"""

import  pendulum # libreria per impostare delle date
from airflow.decorators import task
from airflow.models.dag import DAG
from airflow.operators.empty import EmptyOperator # Operatore vuoto che permette di impostare dei pezzi di inizio e di fine, più per forma che per sostanza

# Instanziamo un DAG
with DAG(
    dag_id="my_first_dag",
    start_date=pendulum.datetime(2021, 1,1),
    catchup=False,  
    #se si inserisce una data precedente e si schedula che il dag debba girare tutti i giorni, fa partire le esecuz. passate che deve recuperare ma non va bene
    schedule=None

) as dag:
    inizio=EmptyOperator(task_id="inizio")
# Salviamo da file -> Salva e poi andiamo in airflow e aggiorniamo_ dorebbe esserci il dag, possiamo cercarlo
# Vediamo solo "inizio" a sx

# Aggiungiamo un decoratore: che arricchisce una funzione con qualcos'altro
    @task()    # con task diventa un operatore di airflow, se non ci fosse, load_dataset sarebbe una semplice funzione python
    def load_dataset():
        print("loading dataset...")
        print("dataset loaded")
        return "path/to/dataset.parquet"

    load_dataset_task=load_dataset()
# task per l'esercitazione
    @task.branch()
    def check_path(dataset_path):
        if dataset_path:
            return "training_ML_Model"
        else:
            return "raise_error_dataset_path"

    check_path_task=check_path(load_dataset_task)


# Secondo task che aggiungo
    @task(task_id="training_ML_Model")   # per convenzione e semplicità il task id ha lo stesso nome della funzione
    def training_ML_Model(dataset_path):
        print(f"readinf dataset from {dataset_path}")
        print("dataset letto")
        print("modello addestrato")
        return "ML_flow_model_id"

    training_ML_Model_task= training_ML_Model(load_dataset_task)

    @task(task_id="raise_error_dataset_path")
    def raise_error_dataset_path():
        raise Exception("Percorso del dataset nullo")

    raise_error_dataset_path_task=raise_error_dataset_path()

    # Aggiorniamo la pagine dag di airflow: vedo le de task inizio e load_dataset che però al momento sono scollegate, quindi verrebbero eseguite in contemporanea
    # Aggiungo le dipendenze:
    inizio >> load_dataset_task >> check_path_task >> [training_ML_Model_task,raise_error_dataset_path_task]

    # le ultime due task dipendono dal task precedente: è una lista e avremo o una task o l'altra

    # Se premo il tasto g mentre sono dentro la dag, si apre il grafo
# Per aggiornare il dag, su airflow: reparse dag in alto a sx e poi trigger: se tutte le caselle del grafo sono verdi, è andato tutto bene