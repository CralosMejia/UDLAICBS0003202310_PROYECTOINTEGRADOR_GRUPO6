from Data.seed import *
from ETL.extract.extractions import extracciones
from ETL.load.loads import cargas
from ETL.transform.transformations import transformaciones
from util.connection import connect
from util.properties import getProperty
import time


# ABRIR CONEXIONES
name_DB_source = getProperty("DATABASESOURCENAME")
ses_db_source = connect(name_DB_source);

name_DB_stg = getProperty("DATABASESTGNAME")
ses_db_stg = connect(name_DB_stg);

name_DB_sor = getProperty("DATABASESORNAME")
ses_db_sor= connect(name_DB_sor);


# CARGAR EL SEED
t0 = time.perf_counter()
cargarDataAleatoria(ses_db_source)
t1 = time.perf_counter()
print(f"Cargar data aleatoria: {t1 - t0} sec")

#CARGAR EL EXTRACT
t0 = time.perf_counter()
extracciones(ses_db_stg,ses_db_source)
t1 = time.perf_counter()
print(f"Extracciones: {t1 - t0} sec")

#CARGAR EL transform
t0 = time.perf_counter()
transformaciones(ses_db_stg)
t1 = time.perf_counter()
print(f"Transformaciones: {t1 - t0} sec")

#CARGAR EL LOAD
t0 = time.perf_counter()
cargas(ses_db_stg,ses_db_sor)
t1 = time.perf_counter()
print(f"Carga al sor: {t1 - t0} sec")

# CERRAR CONEXIONES
ses_db_source.dispose()
ses_db_stg.dispose()
ses_db_sor.dispose()

