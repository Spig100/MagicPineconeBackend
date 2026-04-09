from fastapi import FastAPI
from contextlib import asynccontextmanager

from routers import test, course
from database.db_connect import engine
from database.models import Base
from internal.scheduler import start_scheduler, scheduler
import logging

logging.basicConfig(level=logging.INFO)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    Base.metadata.create_all(bind=engine)
    start_scheduler()
    yield
    # Shutdown
    scheduler.shutdown()

app = FastAPI(
    title='Magic Pinecone Backend API',
    description='A project allows NCUers to retrieval the massive campus information in this single platform.',
    version='0.0.0',
    contact={
        'name': 'Shawn Lin',
        'email': 'spig100.roc@gmail.com'
    },
    lifespan=lifespan
)

app.include_router(test.router)
app.include_router(course.router)

@app.get("/")
def root():
    return {"message": "Welcome to Amazing Pinecone Backend!"}