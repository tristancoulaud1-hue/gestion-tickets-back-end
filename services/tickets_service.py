import json
from pathlib import Path
from math import ceil
from datetime import date
from typing import Optional

DATA_PATH = Path(__file__).parent.parent / "data" / "tickets.json"

def read_tickets():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def write_tickets(tickets):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(tickets, f, indent=2, ensure_ascii=False)

def add_ticket(new_ticket: dict):
    tickets = read_tickets()

    new_id = max(ticket["id"] for ticket in tickets) + 1 if tickets else 1
    new_ticket["id"] = new_id

    new_ticket["createdAt"] = date.today().isoformat() 

    tickets.append(new_ticket)
    write_tickets(tickets)

    return new_ticket
def add_ticket(new_ticket: dict):
    tickets = read_tickets()

    new_id = max(ticket["id"] for ticket in tickets) + 1 if tickets else 1
    new_ticket["id"] = new_id

    tickets.append(new_ticket)
    write_tickets(tickets)


    return new_ticket

def update_ticket(ticket_id: int, updated_fields: dict):
    tickets = read_tickets()

    for ticket in tickets:
        if ticket["id"] == ticket_id:
            ticket.update(updated_fields)
            write_tickets(tickets)
            return ticket

    return None

def delete_ticket(ticket_id: int):
    tickets = read_tickets()

    for i, ticket in enumerate(tickets):
        if ticket["id"] == ticket_id:
            deleted_ticket = tickets.pop(i)
            write_tickets(tickets)
            return deleted_ticket

    return None

def query_tickets(
    status: Optional[str] = None,
    priority: Optional[str] = None,
    tag: Optional[str] = None,
    search: Optional[str] = None,
    fromDate: Optional[str] = None,
    toDate: Optional[str] = None,
    sortBy: Optional[str] = None,
    order: str = "asc",
    page: int = 1,
    limit: int = 5,
):
    tickets = read_tickets()

    # 🔍 Filtres
    if status:
        tickets = [t for t in tickets if t.get("status") == status]

    if priority:
        tickets = [t for t in tickets if t.get("priority") == priority]

    if tag:
        tickets = [t for t in tickets if tag in t.get("tags", [])]

    if search:
        s = search.lower()
        tickets = [
            t for t in tickets
            if s in (t.get("title", "").lower())
            or s in (t.get("description", "").lower())
        ]

    if fromDate:
        tickets = [t for t in tickets if t.get("createdAt", "") >= fromDate]

    if toDate:
        tickets = [t for t in tickets if t.get("createdAt", "") <= toDate]

    if sortBy:
        reverse = (order == "desc")

        allowed_sort_fields = {"createdAt", "title", "priority", "status", "id"}
        if sortBy not in allowed_sort_fields:
            raise ValueError("Invalid sort field")

        tickets = sorted(tickets, key=lambda x: x.get(sortBy) or "", reverse=reverse)

    # Pagination
    total = len(tickets)
    pages = ceil(total / limit) if limit > 0 else 1
    if page < 1:
        page = 1
    if limit < 1:
        limit = 5

    start = (page - 1) * limit
    end = start + limit
    paginated = tickets[start:end]


    return {
        "page": page,
        "limit": limit,
        "total": total,
        "pages": pages,
        "data": paginated,
    }
