from fastapi import APIRouter

router = APIRouter(
    prefix="/course",
    tags=['Users']
)

@router.get('/find')
async def find_course():
    pass