import pandas as pd

from ETL.util.sql import merge

def cargarProfesoresSor(ses_db_stg,ses_db_sor):
    # definicion del diccionario
    profesoresDict = {
        "id": [],
        "nombre_completo": [],
        "genero": [],
        "direccion": [],
        "telefono": [],
        "cedula": [],
        "sueldo": [],
        "cod_etl": [],
    }

    # Reading the ext table
    profesor_tra_tabla = pd.read_sql(
        f"SELECT id,nombre_completo,genero,direccion,telefono,cedula,sueldo,cod_etl FROM profesor_tra",
        ses_db_stg)

    if not profesor_tra_tabla.empty:
        for id,nombre_completo,genero,direccion,telefono,cedula,sueldo,cod_etl in zip(
                profesor_tra_tabla["id"],
                profesor_tra_tabla["nombre_completo"],
                profesor_tra_tabla["genero"],
                profesor_tra_tabla["direccion"],
                profesor_tra_tabla["telefono"],
                profesor_tra_tabla["cedula"],
                profesor_tra_tabla["sueldo"],
                profesor_tra_tabla["cod_etl"],

        ):
            profesoresDict["id"].append(id)
            profesoresDict["nombre_completo"].append(nombre_completo)
            profesoresDict["genero"].append(genero)
            profesoresDict["direccion"].append(direccion)
            profesoresDict["telefono"].append(telefono)
            profesoresDict["cedula"].append(cedula)
            profesoresDict["sueldo"].append(sueldo)
            profesoresDict["cod_etl"].append(cod_etl)

    if profesoresDict["id"]:
        profesorDF_tra = pd.DataFrame(profesoresDict)
        merge(table_name='profesor_dim', natural_key_cols=['id'], dataframe=profesorDF_tra,db_context=ses_db_sor);
    ses_db_stg.dispose()
    ses_db_sor.dispose()