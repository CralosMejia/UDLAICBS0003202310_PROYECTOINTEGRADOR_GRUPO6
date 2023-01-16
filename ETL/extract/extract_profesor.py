import pandas as pd


def extraerProfesores(ses_db_stg,ses_db_source):
    # definicion del diccionario
    profesoresDict = {
        "id": [],
        "nombre": [],
        "genero": [],
        "segundo_nombre": [],
        "apellido_paterno": [],
        "apellido_materno": [],
        "direccion": [],
        "telefono": [],
        "cedula": [],
        "sueldo": []
    }

    # Reading the ext table
    profesor_ext_tabla = pd.read_sql(
        f"SELECT id,nombre,genero,segundo_nombre,apellido_paterno,apellido_materno,direccion,telefono,cedula,sueldo FROM profesor",
        ses_db_source)

    if not profesor_ext_tabla.empty:
        for id, nombre, genero, segundo_nombre, apellido_paterno, apellido_materno, direccion, telefono, cedula,sueldo in zip(
                profesor_ext_tabla["id"],
                profesor_ext_tabla["nombre"],
                profesor_ext_tabla["genero"],
                profesor_ext_tabla["segundo_nombre"],
                profesor_ext_tabla["apellido_paterno"],
                profesor_ext_tabla["apellido_materno"],
                profesor_ext_tabla["direccion"],
                profesor_ext_tabla["telefono"],
                profesor_ext_tabla["cedula"],
                profesor_ext_tabla["sueldo"],

        ):
            profesoresDict["id"].append(id)
            profesoresDict["nombre"].append(nombre)
            profesoresDict["genero"].append(genero)
            profesoresDict["segundo_nombre"].append(segundo_nombre)
            profesoresDict["apellido_paterno"].append(apellido_paterno)
            profesoresDict["apellido_materno"].append(apellido_materno)
            profesoresDict["direccion"].append(direccion)
            profesoresDict["telefono"].append(telefono)
            profesoresDict["cedula"].append(cedula)
            profesoresDict["sueldo"].append(sueldo)


    if profesoresDict["id"]:
        ses_db_stg.connect().execute('TRUNCATE TABLE profesor_ext')
        profesorDF_ext = pd.DataFrame(profesoresDict)
        profesorDF_ext.to_sql('profesor_ext', ses_db_stg, if_exists='append', index=False)
    ses_db_stg.dispose()
    ses_db_source.dispose()