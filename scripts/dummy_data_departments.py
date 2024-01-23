import os
import random
from dataclasses import astuple

from faker import Faker
from faker.providers import DynamicProvider

from db import cursor
from models.department import Department

schema_name = os.getenv('SCHEMA_NAME', 'inexistent_schema')


if __name__ == '__main__':
    faker = Faker()
    end_range = 1000

    companies_id = cursor.execute(
        f'select id from [{schema_name}].company'
    ).fetchall()

    tuple_factory = lambda x: tuple(
        [value for value in x if value is not None]
    )

    departments = []
    company_department = DynamicProvider(
        provider_name='company_department',
        elements=[
            'Accounting',
            'HR',
            'Marketing',
            'Sales',
            'IT',
            'ResearchAndDevelopment',
            'CustomerService',
            'Purchasing',
            'Legal',
            'Production',
            'QA',
            'Shipping',
            'Maintenance',
            'Engineering',
        ],
    )
    faker.add_provider(company_department)

    for _ in range(1, end_range):  # 1, 999
        departments.append(
            astuple(
                Department(
                    department_name=faker.company_department(),
                    department_description='Lorem Ipsum',
                    company_id=random.choice(list(companies_id))[0],
                ),
                tuple_factory=tuple_factory,
            )
        )

    cursor.executemany(
        (
            f'insert into [{schema_name}].department '
            '(department_name, department_description, company_id) values (?,?,?)'
        ),
        departments,
    )
    cursor.commit()
