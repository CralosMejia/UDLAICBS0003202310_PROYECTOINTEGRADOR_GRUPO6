import pandas as pd

from ETL.util.sql import merge


def cargarAreasAcademicasSor(ses_db_stg,ses_db_sor):
    areasAcademicas_dict = {
        "id": [],
        "nombre": [],
        "cod_etl": [],
    }

    # Reading the ext table
    area_academica_tra_tabla = pd.read_sql(
        f"SELECT id,nombre,cod_etl FROM area_acad_tra",
        ses_db_stg)

    if not area_academica_tra_tabla.empty:
        for id,nombre,cod_etl in zip(
            area_academica_tra_tabla["id"],
            area_academica_tra_tabla["nombre"],
            area_academica_tra_tabla["cod_etl"]
        ):
            areasAcademicas_dict["id"].append(id)
            areasAcademicas_dict["nombre"].append(nombre)
            areasAcademicas_dict["cod_etl"].append(cod_etl)

    if areasAcademicas_dict["id"]:
        areasAcademicasDF_tra = pd.DataFrame(areasAcademicas_dict)
        merge(table_name='area_acad_dim', natural_key_cols=['id'], dataframe=areasAcademicasDF_tra, db_context=ses_db_sor);
    ses_db_stg.dispose()
    ses_db_sor.dispose()
