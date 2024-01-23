"""Employee model for the employee table."""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Employee:
    """Employee dataclass model for the employee table."""

    first_name: str
    last_name: str
    birth_date: datetime
    position: str
    hire_date: datetime
    created_at: datetime
    updated_at: datetime
    department_id: int
    salary: int
    id: Optional[int] = None
    leave_date: Optional[datetime] = None
