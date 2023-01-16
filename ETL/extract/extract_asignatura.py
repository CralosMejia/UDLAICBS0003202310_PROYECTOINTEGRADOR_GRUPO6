import pandas as pd

def extraerAsignaturas(ses_db_stg,ses_db_source):
    asignaturas_dict = {
        "id":[],
        "nombre": [],
        "area_academica": []
    }

    # Reading the ext table
    asignatura_ext_tabla = pd.read_sql(
        f"SELECT id,nombre,area_academica FROM asignatura",
        ses_db_source)

    if not asignatura_ext_tabla.empty:
        for id,nombre,area_academica in zip(
            asignatura_ext_tabla["id"],
            asignatura_ext_tabla["nombre"],
            asignatura_ext_tabla["area_academica"],
        ):
            asignaturas_dict["id"].append(id)
            asignaturas_dict["nombre"].append(nombre)
            asignaturas_dict["area_academica"].append(area_academica)

    if asignaturas_dict["id"]:
        ses_db_stg.connect().execute('TRUNCATE TABLE asignatura_ext')
        asignaturaDF_ext = pd.DataFrame(asignaturas_dict)
        asignaturaDF_ext.to_sql('asignatura_ext', ses_db_stg, if_exists='append', index=False)
    ses_db_stg.dispose()
    ses_db_source.dispose()