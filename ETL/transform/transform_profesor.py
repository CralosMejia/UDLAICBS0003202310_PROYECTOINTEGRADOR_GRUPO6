import pandas as pd

from ETL.transform.transformData import transformarNombreCompleto, transformarGenero, \
    estandarizarSueldos


def transformacionProfesor(ses_db_stg,cod_etl):
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
    profesor_ext_tabla = pd.read_sql(
        f"SELECT id,nombre,genero,segundo_nombre,apellido_paterno,apellido_materno,direccion,telefono,cedula,sueldo FROM profesor_ext",
        ses_db_stg)

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
            profesoresDict["nombre_completo"].append(transformarNombreCompleto(nombre, segundo_nombre, apellido_paterno, apellido_materno))
            profesoresDict["genero"].append(transformarGenero(genero))
            profesoresDict["direccion"].append(direccion)
            profesoresDict["telefono"].append(telefono)
            profesoresDict["cedula"].append(cedula)
            profesoresDict["sueldo"].append(estandarizarSueldos(sueldo))
            profesoresDict["cod_etl"].append(cod_etl)

    if profesoresDict["id"]:
        profesorDF_ext = pd.DataFrame(profesoresDict)
        profesorDF_ext.to_sql('profesor_tra', ses_db_stg, if_exists='append', index=False)
    ses_db_stg.dispose()