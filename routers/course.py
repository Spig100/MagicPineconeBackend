from fastapi import APIRouter

router = APIRouter(
    prefix="/course",
    tags=["Users"]
)

@router.get("/")
async def get_courses():
