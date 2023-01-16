from ETL.load.load_area_academica import cargarAreasAcademicasSor
from ETL.load.load_asignatura import cargarAsignaturaSor
from ETL.load.load_calificacion import cargarCalificacionSor
from ETL.load.load_estudiante import cargarEstudiantesSor
from ETL.load.load_profesores import cargarProfesoresSor


def cargas(ses_db_stg,ses_db_sor):
    cargarAreasAcademicasSor(ses_db_stg, ses_db_sor)
    cargarEstudiantesSor(ses_db_stg, ses_db_sor)
    cargarProfesoresSor(ses_db_stg, ses_db_sor)
    cargarAsignaturaSor(ses_db_stg, ses_db_sor)
    cargarCalificacionSor(ses_db_stg, ses_db_sor)
