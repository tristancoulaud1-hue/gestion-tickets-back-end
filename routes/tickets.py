from fastapi import APIRouter, HTTPException
from services.tickets_service import (read_tickets, add_ticket, update_ticket, delete_ticket, query_tickets)
from models.ticket import (TicketCreate, TicketUpdate)
from typing import Optional
from math import ceil

router = APIRouter()

@router.get("/tickets")
def get_tickets(
    status: Optional[str] = None,
    priority: Optional[str] = None,
    tag: Optional[str] = None,
    search: Optional[str] = None,
    fromDate: Optional[str] = None,
    toDate: Optional[str] = None,
    sortBy: Optional[str] = None,
    order: Optional[str] = "asc",
    page: int = 1,
    limit: int = 5,
):
    try:
        return query_tickets(
            status=status,
            priority=priority,
            tag=tag,
            search=search,
            fromDate=fromDate,
            toDate=toDate,
            sortBy=sortBy,
            order=order or "asc",
            page=page,
            limit=limit,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/tickets")
def create_ticket(ticket: TicketCreate):
    return add_ticket(ticket.model_dump())

@router.patch("/tickets/{ticket_id}")
def patch_ticket(ticket_id: int, updated_fields: TicketUpdate):
    updated_ticket = update_ticket(ticket_id, updated_fields.dict(exclude_unset=True))

    if not updated_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return updated_ticket

@router.delete("/tickets/{ticket_id}")
def remove_ticket(ticket_id: int):
    deleted_ticket = delete_ticket(ticket_id)

    if not deleted_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return {
        "message": "Ticket deleted successfully",
        "ticket": deleted_ticket
    }

