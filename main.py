from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.tickets import router as tickets_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tickets_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Ticket Management API"}