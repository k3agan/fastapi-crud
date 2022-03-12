from fastapi import APIRouter

router = APIRouter()


@router.get("/sequence")
async def pong():
    # some async operations could happen here
    # example: `notes = await get_notes()`
    return {"sequence": ["pong!0", "pong!1", "pong!2"]}
