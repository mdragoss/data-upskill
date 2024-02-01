import argparse
# from db import cursor
import csv
import os
import sys
import time
from pathlib import Path
from typing import List, Tuple

from pyodbc import Cursor

abs_path = os.path.abspath(os.path.dirname(__name__))
sys.path.append(os.path.join(abs_path, 'fixtures'))

parser = argparse.ArgumentParser(
    prog='Bulk insert with pyodbc or pandas',
    description='Insert bulk data into SQL Server',
)

parser.add_argument(
    'path', default='fixtures', type=Path, help='path to the fixtures folder'
)
parser.add_argument(
    '-f', '--file', default='dataset.csv', help='file name to read data from'
)
parser.add_argument(
    '-t', '--table', help='table name insert data into', required=True
)
parser.add_argument(
    '-s', '--schema', help='schema name where table is', required=True
)
parser.add_argument(
    '--pyodbc', help='use pyodbc to insert data', action='store_true'
)
parser.add_argument(
    '--pandas', help='use pandas to insert data', action='store_true'
)
args = parser.parse_args()


def validate_arguments(pyodbc: bool, pandas: bool):
    if pyodbc and pandas:
        print('You can only use one of the options --pyodbc or --pandas')
        sys.exit(1)
    elif not pyodbc and not pandas:
        print('You must use one of the options --pyodbc or --pandas')
        sys.exit(1)


def validate_schema_and_name(schema: str, table: str):
    result = cursor.execute(
        'select table_name from information_schema.tables where table_schema = ? and table_name = ?',
        schema,
        table,
    )
    if not result.fetchone():
        print(f'Table {table} does not exist in schema {schema}.')
        sys.exit(1)


def validate_file(path: Path, file: str):
    if not path.is_dir():
        print(f'Path {path} does not exist.')
        sys.exit(1)

    if not path.joinpath(file).is_file():
        print(f'File {file} does not exist in path {path}.')
        sys.exit(1)


def time_function(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(
            f'Function {func.__name__} took {end - start} seconds to complete'
        )

    return wrapper


@time_function
def insert_with_pyodbc(
    cursor: Cursor,
    fast_execute: bool,
    *,
    columns: List[str],
    dataset: List[Tuple],
    table: str,
    schema: str,
):
    if fast_execute:
        cursor.fast_executemany = True

    column_names = ', '.join(columns)
    values = ', '.join(['?' for _ in range(len(dataset[0]))])

    cursor.executemany(
        f'insert into [{schema}].{table} ({column_names}) values ({values})',
        dataset,
    )
    cursor.commit()


@time_function
def insert_with_pandas():
    pass


if __name__ == '__main__':
    validate_arguments(args.pyodbc, args.pandas)
    validate_schema_and_name(args.schema, args.table)
    validate_file(args.path, args.file)
