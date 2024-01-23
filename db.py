import pyodbc
from config import config

connection = pyodbc.connect(
    Driver=config.DRIVER,
    Server=config.SERVER,
    UID=config.USER,
    PWD=config.PASSwORD,
    Database=config.DATABASE,
    TrustServerCertificate=config.TRUST_SERVER_CERTIFICATE,
)
cursor = connection.cursor()
