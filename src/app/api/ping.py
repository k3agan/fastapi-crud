from fastapi import APIRouter
import os
router = APIRouter()


@router.get("/ping")
def pong():
    return {"ping": "pong!"}

    # return {"ping": os.environ.get("DATABASE_URL")}
