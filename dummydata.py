import pprint
import random
from dataclasses import astuple, dataclass
from datetime import date, datetime
from typing import Optional, Union

from faker import Faker
from faker.providers import DynamicProvider


@dataclass
class Company:
    idno: str
    company_name: str
    website: str
    company_description: str
    created_at: str
    updated_at: str
    founded_year: date
    is_active: int = 1
    id: Optional[int] = None


@dataclass
class Department:
    department_name: str
    department_description: str
    company_id: int
    is_active: int = 1
    id: Optional[int] = None


@dataclass
class Employee:
    first_name: str
    last_name: str
    birth_date: date
    position: str
    hire_date: date
    created_at: str
    updated_at: str
    department_id: int
    salary: int
    id: Optional[int] = None
    leave_date: Union[Optional[date], str] = 'null'


if __name__ == '__main__':
    faker = Faker()
    end_range = 1000

    companies = []
    departments = []
    employees = []

    company_idno = DynamicProvider(
        provider_name='company_idno',
        elements=[
            '1234567890123',
            '1234567891',
            '1233456789123' '1234567894123',
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

    faker.add_provider(company_idno)
    faker.add_provider(company_department)

    tuple_factory = lambda x: tuple(
        [value for value in x if value is not None]
    )

    for _ in range(1, end_range):  # 1, 999
        companies.append(
            astuple(
                Company(
                    id=_,
                    company_name=faker.company(),
                    idno=faker.company_idno(),
                    website=faker.url(),
                    company_description='null',
                    created_at=datetime.utcnow()
                    .replace(second=0, microsecond=0)
                    .isoformat(),
                    updated_at='null',
                    founded_year=faker.date_between(
                        start_date=date(2000, 1, 1), end_date=date(2020, 1, 1)
                    ).isoformat(),
                ),
                tuple_factory=tuple_factory,
            )
        )
        departments.append(
            astuple(
                Department(
                    department_name=faker.company_department(),
                    department_description='null',
                    company_id=random.choice(range(1, end_range)),
                ),
                tuple_factory=tuple_factory,
            )
        )
        employees.append(
            astuple(
                Employee(
                    first_name=faker.first_name(),
                    last_name=faker.last_name(),
                    birth_date=faker.date_between(
                        start_date=date(1990, 1, 1), end_date=date(2011, 1, 1)
                    ).isoformat(),
                    position=faker.job(),
                    hire_date=faker.date_between(
                        start_date=date(2012, 1, 1), end_date=date(2020, 1, 1)
                    ).isoformat(),
                    salary=random.randint(1000, 10000),
                    leave_date='null',
                    created_at=datetime.utcnow().isoformat(),
                    updated_at='null',
                    department_id=random.choice(range(1, end_range)),
                ),
                tuple_factory=tuple_factory,
            )
        )

    # pprint.pprint(companies)
    # pprint.pprint(departments) 
    pprint.pprint(employees)
