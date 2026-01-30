from pydantic import BaseModel
from typing import List, Optional, Literal

class TicketCreate(BaseModel):
    title: str
    description: str
    status: Literal["Open", "In Progress", "Done"]
    priority: Literal["Low", "Medium", "High"]
    tags: List[str]

class TicketUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[Literal["Open", "In Progress", "Done"]] = None
    priority: Optional[Literal["Low", "Medium", "High"]] = None
    tags: Optional[List[str]] = None
    createdAt: Optional[str] = None
