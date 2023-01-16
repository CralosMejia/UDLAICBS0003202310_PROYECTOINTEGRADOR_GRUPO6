import pandas as pd

def extraerAsignaturaProfesor(ses_db_stg,ses_db_source):
    # definicion del diccionario
    asignaturaProfesoresDict = {
        "id": [],
        "asignaturaId": [],
        "profesorId": []
    }

    asignaturaProfesor_ext_tabla = pd.read_sql(
        f"SELECT id,asignaturaId,profesorId FROM asignatura_profesor",
        ses_db_source)

    if not asignaturaProfesor_ext_tabla.empty:
        for id,asignaturaId,profesorId in zip(
            asignaturaProfesor_ext_tabla["id"],
            asignaturaProfesor_ext_tabla["asignaturaId"],
            asignaturaProfesor_ext_tabla["profesorId"],
        ):
            asignaturaProfesoresDict["id"].append(id)
            asignaturaProfesoresDict["asignaturaId"].append(asignaturaId)
            asignaturaProfesoresDict["profesorId"].append(profesorId)

    if asignaturaProfesoresDict["id"]:
        ses_db_stg.connect().execute('TRUNCATE TABLE asignatura_profesor_ext')
        asignaturaProfesorDF_ext = pd.DataFrame(asignaturaProfesoresDict)
        asignaturaProfesorDF_ext.to_sql('asignatura_profesor_ext', ses_db_stg, if_exists='append', index=False)
    ses_db_stg.dispose()
    ses_db_source.dispose()