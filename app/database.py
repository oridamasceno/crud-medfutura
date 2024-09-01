import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

server = os.getenv('DB_SERVER')
database = os.getenv('DB_NAME')
username = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
driver = os.getenv('DB_DRIVER')

connection_string = fconnection_string = "DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost;DATABASE=PessoaDB;UID=oridamasceno;PWD=01Amenic!;DB_PORT=1433;TrustServerCertificate=yes"


def get_db_connection():
    return pyodbc.connect(connection_string)