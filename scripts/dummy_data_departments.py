"""Script to generate dummy data for departments table."""
import os
import random
from dataclasses import astuple

from faker import Faker
from faker.providers import DynamicProvider

from src.db import cursor
from src.helpers.util import tuple_factory
from src.models.department import Department

schema_name = os.getenv('SCHEMA_NAME', 'inexistent_schema')


if __name__ == '__main__':
    faker = Faker()
    END_RANGE = 1000

    companies_id = cursor.execute(
        f'select id from [{schema_name}].company'
    ).fetchall()

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

    for _ in range(1, END_RANGE):  # 1, 999
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

    cursor.fast_executemany = True
    cursor.executemany(
        (
            f'insert into [{schema_name}].department '
            '(department_name, department_description, company_id) values (?,?,?)'
        ),
        departments,
    )
    cursor.commit()
    cursor.close()
