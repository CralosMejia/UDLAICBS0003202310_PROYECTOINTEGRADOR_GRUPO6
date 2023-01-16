import pandas as pd

def transformarNombreCompleto(nombre:str, segundo_nombre:str, apellido_paterno:str, apellido_materno:str):
    return nombre+" "+segundo_nombre+" "+apellido_paterno+" "+apellido_materno;

def transformarGenero(genero:str):
    if genero == "M":
        return "MASCULINO"
    else:
        return "FEMENINO"


def estandarizarFlotantes(numero:str):
    resp = numero.replace(",",".");

    if float(resp) > 10:
        return 10
    return float(resp);

def estandarizarSueldos(numero:str):
    resp = numero.replace(",",".");
    return float(resp);

def obtenerAreaAcademicaID(ses_db_stg,nombreAreaAcademica:str):
    areaAcademica_ext_tabla = pd.read_sql(
        f"SELECT id FROM area_acad_ext WHERE nombre = '{nombreAreaAcademica}' LIMIT 1",
        ses_db_stg)

    return areaAcademica_ext_tabla['id'][0];

def obtenerQuimestre(quimestre:str):
    if quimestre == "Primer Quimestre":
        return 1
    else:
        return 2


# print(estandarizarFlotantes("10.34"))