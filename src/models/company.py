"""Company model"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Company:
    """Company dataclass model for the company table."""

    idno: str
    company_name: str
    website: str
    created_at: datetime
    founded_year: int
    is_active: int
    id: Optional[int] = None
    updated_at: Optional[str] = None
    company_description: Optional[str] = None
