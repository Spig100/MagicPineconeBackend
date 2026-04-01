from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import Session
from database.db_connect import get_db
from internal.course_fetcher import sync_courses_to_db
import logging

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/course",
    tags=['Courses']
)

async def run_sync_task():
    db = next(get_db())
    try:
        logger.info("Manual course sync started from endpoint.")
        await sync_courses_to_db(db)
    except Exception as e:
        logger.error(f"Error in manual sync task: {e}")
    finally:
        db.close()

@router.post('/sync', summary="Trigger Course Synchronization", description="Manually triggers a background synchronization of course data from NCU APIs into the local PostgreSQL database.")
async def manual_sync_courses(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_sync_task)
    return {"status": "sync_started", "message": "Course synchronization has started in the background."}