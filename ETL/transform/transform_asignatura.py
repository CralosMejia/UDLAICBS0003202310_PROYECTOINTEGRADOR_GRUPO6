import pandas as pd

from ETL.transform.transformData import obtenerAreaAcademicaID


def transformacionAsignatura(ses_db_stg,cod_etl):
    asignaturas_dict = {
        "id": [],
        "nombre": [],
        "area_academica": [],
        "cod_etl": [],
    }

    # Reading the ext table
    asignatura_ext_tabla = pd.read_sql(
        f"SELECT id,nombre,area_academica FROM asignatura_ext",
        ses_db_stg)

    if not asignatura_ext_tabla.empty:
        for id,nombre,area_academica in zip(
            asignatura_ext_tabla["id"],
            asignatura_ext_tabla["nombre"],
            asignatura_ext_tabla["area_academica"],
        ):
            asignaturas_dict["id"].append(id)
            asignaturas_dict["nombre"].append(nombre)
            asignaturas_dict["area_academica"].append(obtenerAreaAcademicaID(ses_db_stg,area_academica))
            asignaturas_dict["cod_etl"].append(cod_etl)

    if asignaturas_dict["id"]:
        asignaturaDF_ext = pd.DataFrame(asignaturas_dict)
        asignaturaDF_ext.to_sql('asignatura_tra', ses_db_stg, if_exists='append', index=False)
    ses_db_stg.dispose()