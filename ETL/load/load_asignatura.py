import pandas as pd

from ETL.util.sql import merge

def cargarAsignaturaSor(ses_db_stg,ses_db_sor):
    asignaturas_dict = {
        "id": [],
        "nombre": [],
        "area_academica": [],
        "cod_etl": [],
    }

    # Reading the ext table
    asignatura_tra_tabla = pd.read_sql(
        f"SELECT id,nombre,area_academica,cod_etl FROM asignatura_tra",
        ses_db_stg)

    if not asignatura_tra_tabla.empty:
        for id, nombre, area_academica,cod_etl in zip(
                asignatura_tra_tabla["id"],
                asignatura_tra_tabla["nombre"],
                asignatura_tra_tabla["area_academica"],
                asignatura_tra_tabla["cod_etl"],
        ):
            asignaturas_dict["id"].append(id)
            asignaturas_dict["nombre"].append(nombre)
            asignaturas_dict["area_academica"].append(area_academica)
            asignaturas_dict["cod_etl"].append(cod_etl)

    if asignaturas_dict["id"]:
        asignaturaDF_tra = pd.DataFrame(asignaturas_dict)
        merge(table_name='asignatura_dim', natural_key_cols=['id'], dataframe=asignaturaDF_tra, db_context=ses_db_sor);
    ses_db_stg.dispose()
    ses_db_sor.dispose()