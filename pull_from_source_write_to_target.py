import json
import py_dpz_sqlalchemy_utils
from pathlib import Path
import pandas as pd
import sys

def main():
    print("Starting Main...")

    try:
        project_path = Path(sys._MEIPASS)
    except Exception:
        project_path = (Path(__file__).parents[1])

    json_path = project_path.joinpath('config.json')

    with open(json_path, 'r') as f:
        config = json.load(f)

    table_names = config['APP']['TABLES']

    source_user_name = config['SOURCE_DATABASE']['USERNAME']
    source_password = config['SOURCE_DATABASE']['PASSWORD']
    source_server_name = config['SOURCE_DATABASE']['HOST']
    source_database_name = config['SOURCE_DATABASE']['DB']

    target_user_name = config['TARGET_DATABASE']['USERNAME']
    target_password = config['TARGET_DATABASE']['PASSWORD']
    target_server_name = config['TARGET_DATABASE']['HOST']
    target_database_name = config['TARGET_DATABASE']['DB']

    exit()

    sql_source_database = py_dpz_sqlalchemy_utils.PyDpzSqlAlchemyTools(
        server_name=source_server_name,
        database_name=source_database_name,
        user_name=source_user_name,
        user_password=source_password,
    )

    sql_target_database = py_dpz_sqlalchemy_utils.PyDpzSqlAlchemyTools(
        server_name=target_server_name,
        database_name=target_database_name,
        user_name=target_user_name,
        user_password=target_password,
    )

    sql_source_database.windows_logon()
    sql_source_database.connect_to_server()
    sql_source_connection = sql_source_database.get_sql_connection()

    sql_target_database.windows_logon()
    sql_target_database.connect_to_server()
    sql_target_connection = sql_target_database.get_sql_connection()

    for table in table_names:
        table = table.split('.')
        schema_name = table[0]
        table_name = table[1]

        sql_statement = f"SELECT * FROM [{schema_name}].[{table_name}] ORDERBY"
        source_table_dataframe = pd.read_sql(sql_statement, sql_source_connection)
        source_table_dataframe.to_sql(table_name, schema=schema_name, con=sql_target_connection,
                                      if_exists='replace', index=False)

    sql_source_database.windows_logoff()
    sql_target_database.windows_logoff()



if __name__ == '__main__':
    main()
