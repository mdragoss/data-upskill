"""Department model."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Department:
    """Department dataclass model for the department table."""

    department_name: str
    department_description: str
    company_id: int
    id: Optional[int] = None
