import pandas as pd

def extraerEstudiantes(ses_db_stg,ses_db_source):
    estudianteDict = {
        "id": [],
        "nombre": [],
        "genero": [],
        "segundo_nombre": [],
        "apellido_paterno": [],
        "apellido_materno": [],
        "direccion": [],
        "telefono_rep": [],
        "cedula_rep": [],
    }

    # Reading the ext table
    estudiante_ext_tabla = pd.read_sql(
        f"SELECT id,nombre,genero,segundo_nombre,apellido_paterno,apellido_materno,direccion,telefono_rep,cedula_rep FROM estudiante",
        ses_db_source)

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
            estudianteDict["nombre"].append(nombre)
            estudianteDict["genero"].append(genero)
            estudianteDict["segundo_nombre"].append(segundo_nombre)
            estudianteDict["apellido_paterno"].append(apellido_paterno)
            estudianteDict["apellido_materno"].append(apellido_materno)
            estudianteDict["direccion"].append(direccion)
            estudianteDict["telefono_rep"].append(telefono_rep)
            estudianteDict["cedula_rep"].append(cedula_rep)

    if estudianteDict["id"]:
        ses_db_stg.connect().execute('TRUNCATE TABLE estudiante_ext')
        estudianteDF_ext = pd.DataFrame(estudianteDict)
        estudianteDF_ext.to_sql('estudiante_ext', ses_db_stg, if_exists='append', index=False)
    ses_db_stg.dispose()
    ses_db_source.dispose()

