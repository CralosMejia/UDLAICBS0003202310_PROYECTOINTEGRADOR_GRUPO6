import pandas

def obtener_ProfesorID(ses_db_stg, asignaturaId):
    tabla_asignaturaProfesor = pandas.read_sql(f"SELECT profesorId FROM asignatura_profesor_tra WHERE asignaturaID = {asignaturaId} LIMIT 1", ses_db_stg)

    if (not tabla_asignaturaProfesor.empty):
        id = tabla_asignaturaProfesor['profesorId'][0]
    else:
        id = None;

    return id;



def get_surrogate_key_and_natural_key_pairs(table_name, natural_key_cols, db_context):
    """
    Get the surrogate key value from a set of natural keys (business keys)
    """
    natural_keys_str = ','.join(natural_key_cols)
    return pandas.read_sql_query(f'SELECT surrogate_key, {natural_keys_str} FROM {table_name}', db_context).set_index(natural_key_cols).to_dict()['surrogate_key']

def merge(table_name, natural_key_cols, dataframe, db_context):
    existing_table_key_pairs = get_surrogate_key_and_natural_key_pairs(table_name=table_name, natural_key_cols=natural_key_cols, db_context=db_context)
    columns = dataframe.columns.tolist()
    if len(columns) > 0:
        for natural_key in natural_key_cols:
            columns.remove(natural_key)

    if len(natural_key_cols) == 1:
        dataframe['surrogate_key'] = dataframe.apply(lambda row: existing_table_key_pairs.get(*tuple(row[natural_key_cols].values), None), axis=1)
    else:
        dataframe['surrogate_key'] = dataframe.apply(lambda row: existing_table_key_pairs.get(tuple(row[natural_key_cols].values), None), axis=1)

    elements_to_update = dataframe[dataframe['surrogate_key'].notnull()]
    if not elements_to_update.empty:
        existing_elements = pandas.read_sql_query('SELECT * FROM {table_name} WHERE ID IN ({ids})'.format(table_name=table_name, ids=','.join(elements_to_update['surrogate_key'].astype(str))), db_context)
        elements_to_update = elements_to_update.merge(existing_elements, how='outer', indicator=True).query('_merge == "left_only"').drop('_merge', axis=1)
        update_query = f'UPDATE {table_name} SET {",".join([f"{col} = %s" for col in columns])} WHERE ID = %s'
        for index, row in elements_to_update.iterrows():
            db_context.execute(update_query, tuple(row[columns].values) + (row['surrogate_key'],))

    elements_to_insert = dataframe[dataframe['surrogate_key'].isnull()]
    if not elements_to_insert.empty:
        elements_to_insert.to_sql(table_name, db_context, if_exists='append', index=False)