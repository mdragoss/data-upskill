import argparse
import time
from db import cursor
import csv
import os
import sys
from pathlib import Path
from typing import Generator, List, Tuple

from helpers.util import time_function
from pyodbc import Cursor

abs_path = os.path.abspath(os.path.dirname(__name__))
sys.path.append(os.path.join(abs_path, 'fixtures'))

parser = argparse.ArgumentParser(
    prog='Bulk insert with pyodbc or pandas',
    description='Insert bulk data into SQL Server',
)

# parser.add_argument(
#     'path', default='fixtures', type=Path, help='path to the fixtures folder'
# )
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


def validate_path_and_file(path: Path, file: str):
    if not path.is_dir():
        print(f'Path {path} does not exist.')
        sys.exit(1)

    if not path.joinpath(file).is_file():
        print(f'File {file} does not exist in path {path}.')
        sys.exit(1)

    return os.path.join(path, file)


def validate_file(file_path: str):
    if not os.path.isfile(file_path):
        print(f'File {file_path} does not exist.')
        sys.exit(1)

    return file_path


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
    values = ', '.join(['?' for _ in range(len(columns))])
    del columns

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
    csv_file = validate_file(args.file)
    dataset = []

    with open(csv_file, 'r', newline='') as csvfile:
        read_file = csv.reader(csvfile, delimiter=',')
        columns = next(read_file)
        for row in read_file:
            dataset.append(
                tuple(
                    [
                        (
                            row_data
                            if row_data.lower() != 'null' or row_data == ''
                            else None
                        )
                        for row_data in row
                    ]
                )
            )

    if args.pyodbc:
        insert_with_pyodbc(
            cursor,
            True,
            columns=columns,
            dataset=dataset,
            table=args.table,
            schema=args.schema,
        )
