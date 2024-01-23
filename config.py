from dataclasses import dataclass
import os

@dataclass
class Config:
    DRIVER: str = os.getenv('DRIVER', '{ODBC Driver 18 for SQL Server}')
    SERVER: str = os.getenv('SERVER', '127.0.0.1')
    DATABASE: str = os.getenv('DATABASE', 'default_db')
    USER: str = os.getenv('UID', '')
    PASSwORD: str = os.getenv('PWD', '')
    TRUST_SERVER_CERTIFICATE: str = os.getenv('TRUST_SERVER_CERTIFICATE', 'No')

config = Config()
