import pandas  as pd

def transformacionAsignaturaProfesor(ses_db_stg,cod_etl):
    # definicion del diccionario
    asignaturaProfesoresDict = {
        "id": [],
        "asignaturaId": [],
        "profesorId": [],
        "cod_etl": [],
    }

    asignaturaProfesor_ext_tabla = pd.read_sql(
        f"SELECT id,asignaturaId,profesorId FROM asignatura_profesor_ext",
        ses_db_stg)


    if not asignaturaProfesor_ext_tabla.empty:
        for id,asignaturaId,profesorId in zip(
            asignaturaProfesor_ext_tabla["id"],
            asignaturaProfesor_ext_tabla["asignaturaId"],
            asignaturaProfesor_ext_tabla["profesorId"],
        ):
            asignaturaProfesoresDict["id"].append(id)
            asignaturaProfesoresDict["asignaturaId"].append(asignaturaId)
            asignaturaProfesoresDict["profesorId"].append(profesorId)
            asignaturaProfesoresDict["cod_etl"].append(cod_etl)

    if asignaturaProfesoresDict["id"]:
        asignaturaProfesorDF_ext = pd.DataFrame(asignaturaProfesoresDict)
        asignaturaProfesorDF_ext.to_sql('asignatura_profesor_tra', ses_db_stg, if_exists='append', index=False)
    ses_db_stg.dispose()
