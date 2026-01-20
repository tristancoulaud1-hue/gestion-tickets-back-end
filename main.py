from fastapi import FastAPI
from routes.tickets import router as tickets_router

app = FastAPI()

app.include_router(tickets_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Ticket Management API"}