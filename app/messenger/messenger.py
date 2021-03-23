from fastapi import APIRouter

router = APIRouter()

@router.get("/id/{id}")
def get_user(id):
    pass