import os
import random
from dataclasses import astuple
from datetime import datetime

from faker import Faker

from src.db import cursor
from src.models.employee import Employee

schema_name = os.getenv('SCHEMA_NAME', 'inexistent_schema')

if __name__ == '__main__':
    faker = Faker()
    end_range = 1000

    departments_id = cursor.execute(
        f'select id from [{schema_name}].department'
    ).fetchall()

    tuple_factory = lambda x: tuple(
        [value for value in x if value is not None]
    )
    jobs = [
        'Software Developer',
        'QA',
        'DevOps',
        'Manager',
        'CEO',
        'CTO',
        'Admin',
        'HR',
        'Accountant',
        'Sales',
        'Marketing',
        'Customer Service',
        'Purchasing',
        'Legal',
        'Production',
        'Shipping',
        'Maintenance',
        'Engineering',
    ]

    employees = []
    for _ in range(1, end_range):
        employees.append(
            astuple(
                Employee(
                    first_name=faker.first_name(),
                    last_name=faker.last_name(),
                    birth_date=faker.date_time_between(
                        start_date='-50y', end_date='-18y'
                    ),
                    salary=random.randint(1000, 10000),
                    department_id=random.choice(list(departments_id))[0],
                    created_at=datetime.utcnow().strftime(
                        '%Y-%m-%d %H:%M:%S.%f'
                    )[0:-3],
                    position=random.choice(jobs),
                    hire_date=faker.date_time_between(
                        start_date='-10y', end_date='now'
                    ),
                    updated_at=datetime.utcnow().strftime(
                        '%Y-%m-%d %H:%M:%S.%f'
                    )[0:-3],
                ),
                tuple_factory=tuple_factory,
            )
        )

    cursor.executemany(
        (
            f'insert into [{schema_name}].employee (first_name, '
            'last_name, birth_date, position, hire_date, created_at, '
            'updated_at, department_id, salary) '
            'values (?,?,?,?,?,?,?,?,?)'
        ),
        employees,
    )
