from ETL.extract.extract_areas_academicas import extraerAreasAcademicas
from ETL.extract.extract_asignatura import extraerAsignaturas
from ETL.extract.extract_asignatura_profesor import extraerAsignaturaProfesor
from ETL.extract.extract_calificaciones import extraerCalificaciones
from ETL.extract.extract_estudiante import extraerEstudiantes
from ETL.extract.extract_profesor import extraerProfesores

def extracciones(ses_db_stg,ses_db_source):
    extraerAsignaturas(ses_db_stg, ses_db_source)
    extraerEstudiantes(ses_db_stg, ses_db_source)
    extraerCalificaciones(ses_db_stg, ses_db_source)
    extraerProfesores(ses_db_stg, ses_db_source)
    extraerAsignaturaProfesor(ses_db_stg, ses_db_source)
    extraerAreasAcademicas(ses_db_stg, ses_db_source)