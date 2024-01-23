import os

from faker import Faker

from db import cursor

schema_name = os.getenv('SCHEMA_NAME', 'inexistent_schema')

if __name__ == '__main__':
    faker = Faker()
    end_range = 1000

    departments_id = cursor.execute(
        f'select id from [{schema_name}].department'
    ).fetchall()

    employees = []
