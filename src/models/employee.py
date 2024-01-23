from dataclasses import dataclass
from datetime import date
from typing import Optional, Union


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
    leave_date: Optional[date] = None
