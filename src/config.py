"""Config dataclass."""
import os
from dataclasses import dataclass


@dataclass
class Config:
    """Config dataclass for database connection."""

    driver: str = os.getenv('DRIVER', '{ODBC Driver 18 for SQL Server}')
    server: str = os.getenv('SERVER', '127.0.0.1')
    database: str = os.getenv('DATABASE', 'default_db')
    user: str = os.getenv('USER', '')
    password: str = os.getenv('PASS', '')
    trust_server_certificate: str = os.getenv('TRUST_SERVER_CERTIFICATE', 'No')


config = Config()
