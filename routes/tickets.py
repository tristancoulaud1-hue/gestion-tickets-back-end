from fastapi import APIRouter, HTTPException
from services.tickets_service import (
    read_tickets,
    add_ticket,
    update_ticket,
    delete_ticket,
)
from models.ticket import TicketCreate, TicketUpdate
from typing import Optional

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
):
    tickets = read_tickets()

    if status:
        tickets = [t for t in tickets if t["status"] == status]

    if priority:
        tickets = [t for t in tickets if t["priority"] == priority]

    if tag:
        tickets = [t for t in tickets if tag in t.get("tags", [])]

    if search:
        search_lower = search.lower()
        tickets = [
            t for t in tickets
            if search_lower in t["title"].lower()
            or search_lower in t["description"].lower()
        ]

    if fromDate:
        tickets = [t for t in tickets if t["createdAt"] >= fromDate]

    if toDate:
        tickets = [t for t in tickets if t["createdAt"] <= toDate]

    if sortBy:
        try:
            tickets = sorted(tickets, key=lambda x: x.get(sortBy))
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid sort field")

    return tickets

@router.post("/tickets")
def create_ticket(ticket: TicketCreate):
    return add_ticket(ticket.dict())

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

