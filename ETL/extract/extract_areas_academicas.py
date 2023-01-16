import pandas as pd

def extraerAreasAcademicas(ses_db_stg,ses_db_source):
    areasAcademicas_dict = {
        "id": [],
        "nombre": []
    }

    # Reading the csv file
    areasAcademicas_csv = pd.read_csv("Data/csvs/AreasAcademicas.csv")

    if not areasAcademicas_csv.empty:
        for id,nombre in zip(
            areasAcademicas_csv["id"],
            areasAcademicas_csv["nombre"]
        ):
            areasAcademicas_dict["id"].append(id)
            areasAcademicas_dict["nombre"].append(nombre)

    if areasAcademicas_dict["id"]:
        ses_db_stg.connect().execute('TRUNCATE TABLE area_acad_ext')
        areasAcademicasDF_ext = pd.DataFrame(areasAcademicas_dict)
        areasAcademicasDF_ext.to_sql('area_acad_ext', ses_db_stg, if_exists='append', index=False)
    ses_db_stg.dispose()
    ses_db_source.dispose()