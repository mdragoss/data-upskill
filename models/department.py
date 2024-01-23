from dataclasses import dataclass
from typing import Optional


@dataclass
class Department:
    department_name: str
    department_description: str
    company_id: int
    id: Optional[int] = None
