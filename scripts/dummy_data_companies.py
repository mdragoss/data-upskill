import os
import random
from dataclasses import astuple
from datetime import date, datetime

from faker import Faker
from faker.providers import DynamicProvider

from db import cursor
from models.company import Company
from models.department import Department
from models.employee import Employee

schema_name = os.getenv('SCHEMA_NAME', 'inexistent_schema')

if __name__ == '__main__':
    faker = Faker()
    end_range = 1000

    companies = []
    company_idno = DynamicProvider(
        provider_name='company_idno',
        elements=[
            '1234567890123',
            '1234567891',
            '1234567894123',
            '1234567895123',
            '1234567896123',
            '1234567897123',
            '2234567898123',
            '3234567899123',
            '4234567890123',
            '5234567891125',
            '6234567892123',
            '7234567893126',
            '8234567894123',
        ],
    )

    faker.add_provider(company_idno)

    tuple_factory = lambda x: tuple(
        [value for value in x if value is not None]
    )

    for _ in range(1, end_range):  # 1, 999
        companies.append(
            astuple(
                Company(
                    company_name=faker.company(),
                    idno=faker.company_idno(),
                    website=faker.url(),
                    created_at=datetime.utcnow()
                    .replace(second=0, microsecond=0)
                    .strftime('%Y-%m-%d %H:%M:%S.%f')[0:-3],
                    is_active=1,
                    founded_year=random.randint(2000, 2020),
                ),
                tuple_factory=tuple_factory,
            )
        )

    cursor.executemany(
        f'insert into [{schema_name}].company (idno, company_name, website, '
        'created_at, founded_year, is_active) values (?, ?, ?, ?, ?, ?)',
        companies,
    )
    cursor.commit()
