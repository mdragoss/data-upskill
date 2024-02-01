"""Create connection and cursor to the database."""
import pyodbc

from config import config  # pylint: disable=import-error

connection = pyodbc.connect(
    Driver=config.driver,
    Server=config.server,
    UID=config.user,
    PWD=config.password,
    Database=config.database,
    TrustServerCertificate=config.trust_server_certificate,
    ColumnEncryption='Enabled',
)
cursor = connection.cursor()
