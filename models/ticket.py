from pydantic import BaseModel
from typing import List, Optional, Literal

class TicketBase(BaseModel):
    title: str
    description: str
    status: Literal["Open", "In progress", "Done", "Backlog"]
    priority: Literal["Low", "Medium", "High"]
    tags: List[str]
    createdAt: str

class TicketCreate(TicketBase):
    pass

class TicketUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[Literal["Open", "In progress", "Done", "Backlog"]] = None
    priority: Optional[Literal["Low", "Medium", "High"]] = None
    tags: Optional[List[str]] = None
    createdAt: Optional[str] = None