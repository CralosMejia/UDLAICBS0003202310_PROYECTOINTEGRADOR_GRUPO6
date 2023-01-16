import pandas as pd

from ETL.transform.transformData import estandarizarFlotantes, obtenerQuimestre


def transformacionCalificaciones(ses_db_stg,cod_etl):
    calificacionesDict = {
        "id": [],
        "nombre": [],
        "calificacion": [],
        "quimestre": [],
        "asignaturaId": [],
        "estudianteId": [],
        "cod_etl": []
    }

    calificaciones_ext_tabla = pd.read_sql(
        f"SELECT id,nombre,calificacion,quimestre,asignaturaId,estudianteId FROM calificacion_ext",
        ses_db_stg)

    if not calificaciones_ext_tabla.empty:
        for id,nombre,calificacion,quimestre,asignaturaId,estudianteId in zip(
            calificaciones_ext_tabla["id"],
            calificaciones_ext_tabla["nombre"],
            calificaciones_ext_tabla["calificacion"],
            calificaciones_ext_tabla["quimestre"],
            calificaciones_ext_tabla["asignaturaId"],
            calificaciones_ext_tabla["estudianteId"],
        ):
            calificacionesDict["id"].append(id)
            calificacionesDict["nombre"].append(nombre)
            calificacionesDict["calificacion"].append(estandarizarFlotantes(calificacion))
            calificacionesDict["quimestre"].append(obtenerQuimestre(quimestre))
            calificacionesDict["asignaturaId"].append(asignaturaId)
            calificacionesDict["estudianteId"].append(estudianteId)
            calificacionesDict["cod_etl"].append(cod_etl)

    if calificacionesDict["id"]:
        calificacionesDF_ext = pd.DataFrame(calificacionesDict)
        calificacionesDF_ext.to_sql('calificacion_tra', ses_db_stg, if_exists='append', index=False)
    ses_db_stg.dispose()