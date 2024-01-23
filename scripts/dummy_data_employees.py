from faker import Faker

import os

schema_name = os.getenv('SCHEMA_NAME', 'inexistent_schema')

if __name__ == '__main__':
    faker = Faker()
    end_range = 1000

    employees = []
