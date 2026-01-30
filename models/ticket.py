from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import date

class TicketBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=10, max_length=1000)
    status: Literal["Open", "In progress", "Done"]
    priority: Literal["Low", "Medium", "High"]
    tags: List[str] = Field(..., max_items=10)

class TicketCreate(TicketBase):
    pass

class TicketUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, min_length=10, max_length=1000)
    status: Optional[Literal["Open", "In progress", "Done"]] = None
    priority: Optional[Literal["Low", "Medium", "High"]] = None
    tags: Optional[List[str]] = Field(None, max_items=10)
