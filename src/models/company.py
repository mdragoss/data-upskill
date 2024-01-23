from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Company:
    idno: str
    company_name: str
    website: str
    created_at: str
    founded_year: int
    is_active: int
    id: Optional[int] = None
    updated_at: Optional[str] = None
    company_description: Optional[str] = None
