import random

import pandas as pd
from Data.generateData import *

from ETL.Data.generateData import obtenerNombreCalificacion, obtenerCalificacion, obtenerSueldo

NUMERO_ESTUDIANTES=200
NUMERO_PROFESORES=10
NUMERO_CALIFICACIONES_ESTUDIANTES=10
NUMERO_CALIFICACIONES_QUIMESTRE=5

# # ----------------------------------------------------------LOAD ASIGNATURAS----------------------------------------------------------
def cargarAsignaturas(ses_db_source):
    # definicion del diccionario
    asignaturas_dict={
        "nombre":[
            # Area academica Ciencias
            "Biología","Química","Anatomía","Física","Geología",
            # Educación Física
            "Atletismo","Artes Marciales","Natación","Básquetbol","Fútbol",
            # Lenguas Extranjeras
            "Inglés ","Francés ","Portugués","Italiano","Japonés",
            # Informática
            "Tecnología de la información","Ciberseguridad","Robótica","Ofimática","Telemática",
            # Educación Cultural y Artística
            "Danza","Teatro","Pintura","Escultura","Música"


        ],
        "area_academica":[
            "Ciencias","Ciencias","Ciencias","Ciencias","Ciencias",
            "Educación Física","Educación Física","Educación Física","Educación Física","Educación Física",
            "Lenguas Extranjeras","Lenguas Extranjeras","Lenguas Extranjeras","Lenguas Extranjeras","Lenguas Extranjeras",
            "Informática","Informática","Informática","Informática","Informática",
            "Educación Cultural y Artística","Educación Cultural y Artística","Educación Cultural y Artística","Educación Cultural y Artística","Educación Cultural y Artística",
        ]
    }
    # trasnformar de un diccionario a un df
    ses_db_source.connect().execute('SET FOREIGN_KEY_CHECKS = 0')
    ses_db_source.connect().execute('TRUNCATE TABLE asignatura')
    asignaturasDF = pd.DataFrame(asignaturas_dict)
    asignaturasDF.to_sql('asignatura',ses_db_source,if_exists='append',index=False)

# # ----------------------------------------------------------LOAD ESTUDIANTES----------------------------------------------------------
def cargarEstudiantes(ses_db_source):
    # definicion del diccionario
    estudianteDict={
       "nombre": [],
       "genero": [],
       "segundo_nombre": [],
       "apellido_paterno": [],
       "apellido_materno": [],
       "direccion": [],
       "telefono_rep": [],
       "cedula_rep": [],
    }
    #Agregar datos al diccionario
    for i in range(NUMERO_ESTUDIANTES):
        genero = obtenerGenero();
        estudianteDict["nombre"].append(obtenerNombre(genero))
        estudianteDict["genero"].append(genero)
        estudianteDict["segundo_nombre"].append(obtenerNombre(genero))
        estudianteDict["apellido_paterno"].append(obtenerApellido())
        estudianteDict["apellido_materno"].append(obtenerApellido())
        estudianteDict["direccion"].append(obtenerDireccion())
        estudianteDict["telefono_rep"].append(obtenerTelefono())
        estudianteDict["cedula_rep"].append(obtenerCedula())

    # trasnformar de un diccionario a un df
    ses_db_source.connect().execute('SET FOREIGN_KEY_CHECKS = 0')
    ses_db_source.connect().execute('TRUNCATE TABLE estudiante')
    estudianteDF = pd.DataFrame(estudianteDict)
    estudianteDF.to_sql('estudiante',ses_db_source,if_exists='append',index=False)


# # ----------------------------------------------------------LOAD CALIFICACIONES----------------------------------------------------------
def cargarCalificaciones(ses_db_source):
    # definicion del diccionario
    calificacionesDict={
       "nombre": [],
       "calificacion": [],
       "quimestre": [],
       "asignaturaId": [],
       "estudianteId": []
    }
    #Agregar datos al diccionario
    for i in range(NUMERO_ESTUDIANTES):
        for e in range(NUMERO_CALIFICACIONES_ESTUDIANTES):
            calificacionesDict["nombre"].append(obtenerNombreCalificacion())
            calificacionesDict["calificacion"].append(obtenerCalificacion())
            if e >=0 and e<=NUMERO_CALIFICACIONES_QUIMESTRE-1:
                calificacionesDict["quimestre"].append("Primer Quimestre")
            else:
                calificacionesDict["quimestre"].append("Segundo Quimestre")
            calificacionesDict["asignaturaId"].append(random.randint(1,25))
            calificacionesDict["estudianteId"].append(i+1)

    # trasnformar de un diccionario a un df
    ses_db_source.connect().execute('SET FOREIGN_KEY_CHECKS = 0')
    ses_db_source.connect().execute('TRUNCATE TABLE calificacion')
    calificacionesDF = pd.DataFrame(calificacionesDict)
    calificacionesDF.to_sql('calificacion',ses_db_source,if_exists='append',index=False)

# # ----------------------------------------------------------LOAD PROFESORES----------------------------------------------------------
def cargarProfesores(ses_db_source):
    # definicion del diccionario
    profesoresDict = {
        "nombre": [],
        "genero": [],
        "segundo_nombre": [],
        "apellido_paterno": [],
        "apellido_materno": [],
        "direccion": [],
        "telefono": [],
        "cedula": [],
        "sueldo":[]
    }
    # Agregar datos al diccionario
    for i in range(NUMERO_PROFESORES):
        genero = obtenerGenero();
        profesoresDict["nombre"].append(obtenerNombre(genero))
        profesoresDict["genero"].append(genero)
        profesoresDict["segundo_nombre"].append(obtenerNombre(genero))
        profesoresDict["apellido_paterno"].append(obtenerApellido())
        profesoresDict["apellido_materno"].append(obtenerApellido())
        profesoresDict["direccion"].append(obtenerDireccion())
        profesoresDict["telefono"].append(obtenerTelefono())
        profesoresDict["cedula"].append(obtenerCedula())
        profesoresDict["sueldo"].append(obtenerSueldo())

    # trasnformar de un diccionario a un df
    ses_db_source.connect().execute('SET FOREIGN_KEY_CHECKS = 0')
    ses_db_source.connect().execute('TRUNCATE TABLE profesor')
    profesoresDF = pd.DataFrame(profesoresDict)
    profesoresDF.to_sql('profesor', ses_db_source, if_exists='append', index=False)

# # ----------------------------------------------------------LOAD ASIGNATURA PROFESORES----------------------------------------------------------
def cargarAsignaturaProfesores(ses_db_source):
    # definicion del diccionario
    asignaturaProfesoresDict = {
        "asignaturaId": [],
        "profesorId": []
    }
    # Agregar datos al diccionario
    for i in range(25):

        asignaturaProfesoresDict["asignaturaId"].append(i+1)
        if i >= 10:
            asignaturaProfesoresDict["profesorId"].append(random.randint(1,10))
        else:
            asignaturaProfesoresDict["profesorId"].append(i + 1)


    # trasnformar de un diccionario a un df
    ses_db_source.connect().execute('SET FOREIGN_KEY_CHECKS = 0')
    ses_db_source.connect().execute('TRUNCATE TABLE asignatura_profesor')
    asignaturaProfesoresDF = pd.DataFrame(asignaturaProfesoresDict)
    asignaturaProfesoresDF.to_sql('asignatura_profesor', ses_db_source, if_exists='append', index=False)

def cargarDataAleatoria(ses_db_source):
    cargarAsignaturas(ses_db_source);
    cargarEstudiantes(ses_db_source);
    cargarCalificaciones(ses_db_source);
    cargarProfesores(ses_db_source);
    cargarAsignaturaProfesores(ses_db_source);

