import pandas as pd

from ETL.util.sql import merge


def cargarEstudiantesSor(ses_db_stg,ses_db_sor):
    estudianteDict = {
        "id": [],
        "nombre_completo": [],
        "genero": [],
        "direccion": [],
        "telefono_rep": [],
        "cedula_rep": [],
        "cod_etl": [],
    }

    # Reading the ext table
    estudiante_tra_tabla = pd.read_sql(
        f"SELECT id,nombre_completo,genero,direccion,telefono_rep,cedula_rep,cod_etl FROM estudiante_tra",
        ses_db_stg)

    if not estudiante_tra_tabla.empty:
        for id,nombre_completo,genero,direccion,telefono_rep,cedula_rep,cod_etl in zip(
            estudiante_tra_tabla["id"],
            estudiante_tra_tabla["nombre_completo"],
            estudiante_tra_tabla["genero"],
            estudiante_tra_tabla["direccion"],
            estudiante_tra_tabla["telefono_rep"],
            estudiante_tra_tabla["cedula_rep"],
            estudiante_tra_tabla["cod_etl"],
        ):
            estudianteDict["id"].append(id)
            estudianteDict["nombre_completo"].append(nombre_completo)
            estudianteDict["genero"].append(genero)
            estudianteDict["direccion"].append(direccion)
            estudianteDict["telefono_rep"].append(telefono_rep)
            estudianteDict["cedula_rep"].append(cedula_rep)
            estudianteDict["cod_etl"].append(cod_etl)

    if estudianteDict["id"]:
        estudianteDF_tra = pd.DataFrame(estudianteDict)
        merge(table_name='estudiante_dim', natural_key_cols=['id'], dataframe=estudianteDF_tra,db_context=ses_db_sor);
    ses_db_stg.dispose()
    ses_db_sor.dispose()
