import pandas as pd

from ETL.transform.transformData import transformarNombreCompleto, transformarGenero


def trasnformacionEstudiante(ses_db_stg,cod_etl):
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
    estudiante_ext_tabla = pd.read_sql(
        f"SELECT id,nombre,genero,segundo_nombre,apellido_paterno,apellido_materno,direccion,telefono_rep,cedula_rep FROM estudiante_ext",
        ses_db_stg)

    if not estudiante_ext_tabla.empty:
        for id,nombre,genero,segundo_nombre,apellido_paterno,apellido_materno,direccion,telefono_rep,cedula_rep in zip(
            estudiante_ext_tabla["id"],
            estudiante_ext_tabla["nombre"],
            estudiante_ext_tabla["genero"],
            estudiante_ext_tabla["segundo_nombre"],
            estudiante_ext_tabla["apellido_paterno"],
            estudiante_ext_tabla["apellido_materno"],
            estudiante_ext_tabla["direccion"],
            estudiante_ext_tabla["telefono_rep"],
            estudiante_ext_tabla["cedula_rep"],
        ):
            estudianteDict["id"].append(id)
            estudianteDict["nombre_completo"].append(transformarNombreCompleto(nombre, segundo_nombre, apellido_paterno, apellido_materno))
            estudianteDict["genero"].append(transformarGenero(genero))
            estudianteDict["direccion"].append(direccion)
            estudianteDict["telefono_rep"].append(telefono_rep)
            estudianteDict["cedula_rep"].append(cedula_rep)
            estudianteDict["cod_etl"].append(cod_etl)

    if estudianteDict["id"]:
        estudianteDF_ext = pd.DataFrame(estudianteDict)
        estudianteDF_ext.to_sql('estudiante_tra', ses_db_stg, if_exists='append', index=False)
    ses_db_stg.dispose()