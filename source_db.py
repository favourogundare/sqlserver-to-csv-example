import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
load_dotenv()

def get_connection_string():
    connection_string = "mssql+pyodbc:///?odbc_connect=DRIVER={DATABASE_DRIVER};SERVER={DATABASE_HOST};DATABASE={DATABASE_NAME};Trusted_Connection={TRUSTED_CONNECT};"
    connection_string = connection_string.replace("{DATABASE_DRIVER}", os.environ.get("DATABASE_DRIVER"))
    connection_string = connection_string.replace("{DATABASE_HOST}", os.environ.get("DATABASE_HOST"))
    connection_string = connection_string.replace("{DATABASE_NAME}", os.environ.get("DATABASE_NAME"))
    connection_string = connection_string.replace("{TRUSTED_CONNECT}", os.environ.get("TRUSTED_CONNECT"))
    return connection_string


class SourceDB():
    '''Class to connect to the source database'''
    def __init__(self):
        self.connection_string = get_connection_string()
        self.engine = create_engine(self.connection_string)
        self.session = sessionmaker(bind=self.engine)()

    def get_tables(self):
        '''Get all the tables in the database'''
        tables = self.session.execute(text("SELECT * FROM INFORMATION_SCHEMA.TABLES")).fetchall()
        tables = [table[2] for table in tables]
        return tables
    
    def print_tables(self):
        '''pritn all the tables in the database'''
        tables = self.get_tables()
        print('==================================')
        print('Total Tables: ', len(tables))
        for table in tables:
            print('Table: ', table)
    
    def get_columns(self, table_name):
        '''Get all the columns in the table'''
        columns = self.session.execute(text(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'")).fetchall()
        columns = [column[3] for column in columns]
        return columns

    def print_columns(self, table_name):
        '''Print all the columns in the table'''
        columns = self.get_columns(table_name)
        print('==================================')
        print('Table: ', table_name)
        print('Total Columns: ', len(columns))
        for column in columns:
            print('Column: ', column)

    def iterate_table(self, table_name):
        '''
        Iterate over the table
        must return a generator and dictionary
        '''
        # Get the columns
        columns = self.get_columns(table_name)
        # Get the data
        data = self.session.execute(text(f"SELECT * FROM {table_name}")).fetchall()
        # yield the data
        for row in data:
            yield dict(zip(columns, row))
        
    def close(self):
        '''Close the connection'''
        self.session.close()


