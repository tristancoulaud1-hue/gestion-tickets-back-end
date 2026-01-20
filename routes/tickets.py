from fastapi import APIRouter
from services.tickets_service import read_tickets, add_ticket, update_ticket, delete_ticket

router = APIRouter()

@router.get("/tickets")
def get_tickets():
    return read_tickets()

@router.post("/tickets")
def create_ticket(ticket: dict):
    return add_ticket(ticket)

@router.patch("/tickets/{ticket_id}")
def patch_ticket(ticket_id: int, updated_fields: dict):
    uptated_ticket = update_ticket(ticket_id, updated_fields)

    if not uptated_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return uptated_ticket 

@router.delete("/tickets/{ticket_id}")
def remove_ticket(ticket_id: int):
    deleted_ticket = delete_ticket(ticket_id)

    if not deleted_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    return {
        "message": "Ticket deleted successfully",
        "ticket": deleted_ticket
    } 