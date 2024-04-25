from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import players, events
from .database.database import create_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("start")
    create_db()
    yield
    print("quit")

app = FastAPI(lifespan=lifespan)

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(players.router)
app.include_router(events.router)