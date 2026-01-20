import json
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / 'data' / 'tickets.json'

def read_tickets():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_tickets(tickets):
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(tickets, f, indent=2, ensure_ascii=False)

def add_ticket(new_ticket: dict):
    tickets = read_tickets()

    new_id = max(ticket['id'] for ticket in tickets) + 1 if tickets else 1
    new_ticket['id'] = new_id

    tickets.append(new_ticket)
    write_tickets(tickets)

    return new_ticket

def update_ticket(ticket_id: int, updated_fields: dict):
    tickets = read_tickets()
    for ticket in tickets:
        if ticket['id'] == ticket_id:
            ticket.update(updated_fields)
            write_tickets(tickets)
            return ticket
    return None

def delete_ticket(ticket_id: int):
    tickets = read_tickets()

    for i, ticket in enumerate(tickets):
        if ticket['id'] == ticket_id:
            deleted_ticket = tickets.pop(i)
            write_tickets(tickets)
            return deleted_ticket
        
    return None