from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import date

class TicketCreate(BaseModel):
    title: str
    description: str
    status: Literal["Open", "In Progress", "Done"]
    priority: Literal["Low", "Medium", "High"]
    tags: List[str]

class TicketCreate(TicketBase):
    pass

class TicketUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[Literal["Open", "In Progress", "Done"]] = None
    priority: Optional[Literal["Low", "Medium", "High"]] = None
    tags: Optional[List[str]] = None
    createdAt: Optional[str] = None
