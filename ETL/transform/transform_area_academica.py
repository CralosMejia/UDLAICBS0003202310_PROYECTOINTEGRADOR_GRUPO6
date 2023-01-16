import pandas as pd

def transformacionAreaAcademica(ses_db_stg,cod_etl):

    areasAcademicas_dict = {
        "id": [],
        "nombre": [],
        "cod_etl": [],
    }

    # Reading the ext table
    area_academica_ext_tabla = pd.read_sql(
        f"SELECT id,nombre FROM area_acad_ext",
        ses_db_stg)

    if not area_academica_ext_tabla.empty:
        for id,nombre in zip(
            area_academica_ext_tabla["id"],
            area_academica_ext_tabla["nombre"]
        ):
            areasAcademicas_dict["id"].append(id)
            areasAcademicas_dict["nombre"].append(nombre)
            areasAcademicas_dict["cod_etl"].append(cod_etl)

    if areasAcademicas_dict["id"]:
        areasAcademicasDF_ext = pd.DataFrame(areasAcademicas_dict)
        areasAcademicasDF_ext.to_sql('area_acad_tra', ses_db_stg, if_exists='append', index=False)
    ses_db_stg.dispose()
