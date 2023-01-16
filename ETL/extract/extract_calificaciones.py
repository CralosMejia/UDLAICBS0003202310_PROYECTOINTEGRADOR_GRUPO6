import pandas as pd

def extraerCalificaciones(ses_db_stg,ses_db_source):
    calificacionesDict = {
        "id": [],
        "nombre": [],
        "calificacion": [],
        "quimestre": [],
        "asignaturaId": [],
        "estudianteId": []
    }

    calificaciones_ext_tabla = pd.read_sql(
        f"SELECT id,nombre,calificacion,quimestre,asignaturaId,estudianteId FROM calificacion",
        ses_db_source)

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
            calificacionesDict["calificacion"].append(calificacion)
            calificacionesDict["quimestre"].append(quimestre)
            calificacionesDict["asignaturaId"].append(asignaturaId)
            calificacionesDict["estudianteId"].append(estudianteId)

    if calificacionesDict["id"]:
        ses_db_stg.connect().execute('TRUNCATE TABLE calificacion_ext')
        calificacionesDF_ext = pd.DataFrame(calificacionesDict)
        calificacionesDF_ext.to_sql('calificacion_ext', ses_db_stg, if_exists='append', index=False)
    ses_db_stg.dispose()
    ses_db_source.dispose()