import pandas as pd

from ETL.util.sql import merge, obtener_ProfesorID
from datetime import datetime


def cargarCalificacionSor(ses_db_stg,ses_db_sor):
    calificacionesDict = {
        "id": [],
        "nombre": [],
        "calificacion": [],
        "quimestre": [],
        "asignaturaId": [],
        "estudianteId": [],
        "profesorId": [],
        "loadedAt": [],
        "cod_etl": []
    }

    calificaciones_tra_tabla = pd.read_sql(
        f"SELECT id,nombre,calificacion,quimestre,asignaturaId,estudianteId,cod_etl FROM calificacion_tra",
        ses_db_stg)

    if not calificaciones_tra_tabla.empty:
        for id,nombre,calificacion,quimestre,asignaturaId,estudianteId,cod_etl in zip(
                calificaciones_tra_tabla["id"],
                calificaciones_tra_tabla["nombre"],
                calificaciones_tra_tabla["calificacion"],
                calificaciones_tra_tabla["quimestre"],
                calificaciones_tra_tabla["asignaturaId"],
                calificaciones_tra_tabla["estudianteId"],
                calificaciones_tra_tabla["cod_etl"],
        ):
            calificacionesDict["id"].append(id)
            calificacionesDict["nombre"].append(nombre)
            calificacionesDict["calificacion"].append(calificacion)
            calificacionesDict["quimestre"].append(quimestre)
            calificacionesDict["asignaturaId"].append(asignaturaId)
            calificacionesDict["estudianteId"].append(estudianteId)
            calificacionesDict["profesorId"].append(obtener_ProfesorID(ses_db_stg,asignaturaId))
            calificacionesDict["loadedAt"].append(datetime.now())
            calificacionesDict["cod_etl"].append(cod_etl)

    if calificacionesDict["id"]:
        calificacionesDF_tra = pd.DataFrame(calificacionesDict)
        merge(table_name='calificacion_fact', natural_key_cols=['id'], dataframe=calificacionesDF_tra, db_context=ses_db_sor);
    ses_db_stg.dispose()
    ses_db_sor.dispose()