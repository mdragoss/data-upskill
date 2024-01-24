import os
import random

from faker import Faker

from src.db import cursor

schema_name = os.getenv('SCHEMA_NAME', 'inexistent_schema')


def insert_department(departments):
    cursor.fast_executemany = True
    cursor.executemany(
        (
            f'insert into [{schema_name}].department '
            '(department_name, department_description) values (?,?)'
        ),
        departments,
    )
    cursor.commit()


if __name__ == '__main__':
    faker = Faker()
    END_RANGE = 1000

    companies_id = cursor.execute(
        f'select id from [{schema_name}].company'
    ).fetchall()

    departments = []
    company_departments = [
        'Accounting',
        'HR',
        'Marketing',
        'Sales',
        'IT',
        'Research and Development',
        'Customer Service',
        'Purchasing',
        'Legal',
        'Production',
        'QA',
        'Shipping',
        'Maintenance',
        'Engineering',
    ]

    # TODO do not allow insert duplicate departments
    for department in company_departments:
        departments.append((department, f'{department} Description'))

    # insert_department(departments)
    del departments

    department_id = cursor.execute(
        f'select id from [{schema_name}].department'
    ).fetchall()

    start_random = len(company_departments) // 2
    end_random = len(company_departments)

    for company_id in companies_id:
        company_departments = []
        for _ in range(random.randint(start_random, end_random)):
            company_department = (
                company_id[0],
                random.choice(department_id)[0],
            )
            if company_department not in company_departments:
                company_departments.append(company_department)

        cursor.fast_executemany = True
        cursor.executemany(
            (
                f'insert into [{schema_name}].company_department '
                '(company_id, department_id) values (?,?)'
            ),
            company_departments,
        )
        cursor.commit()

    cursor.close()
