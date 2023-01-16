from datetime import datetime
import pandas as pd

from ETL.transform.transform_area_academica import transformacionAreaAcademica
from ETL.transform.transform_asignatura import transformacionAsignatura
from ETL.transform.transform_asignatura_profesor import transformacionAsignaturaProfesor
from ETL.transform.transform_calificacion import transformacionCalificaciones
from ETL.transform.transform_estudiante import trasnformacionEstudiante
from ETL.transform.transform_profesor import transformacionProfesor


def transformaciones(ses_db_stg):
    cod_etl=obtenerCodigoDeProceso(ses_db_stg)
    transformacionAreaAcademica(ses_db_stg,cod_etl)
    trasnformacionEstudiante(ses_db_stg,cod_etl)
    transformacionProfesor(ses_db_stg,cod_etl)
    transformacionAsignatura(ses_db_stg, cod_etl)
    transformacionCalificaciones(ses_db_stg, cod_etl)
    transformacionAsignaturaProfesor(ses_db_stg, cod_etl)

def obtenerCodigoDeProceso(ses_db_stg):
    proceso_dict = {
        "created_at": []
    }

    proceso_dict["created_at"].append(datetime.now())

    df_proceso = pd.DataFrame(proceso_dict)
    df_proceso.to_sql('etl_proc', ses_db_stg, if_exists='append', index=False)

    table_proceso = pd.read_sql('SELECT cod_etl FROM etl_proc ORDER by cod_etl DESC LIMIT 1', ses_db_stg)

    if (not table_proceso.empty):
        id = table_proceso['cod_etl'][0]
    else:
        id = None;

    return id;