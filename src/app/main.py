from fastapi import FastAPI

from app.api import notes, ping, sequence
from app.db import engine, database, metadata

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(ping.router)
app.include_router(sequence.router)
app.include_router(notes.router, prefix="/notes", tags=["notes"])

# Minimum viable (with just the plotly data stuff) graph for testing

# @app.get("/graph")
# def graph():
#     plt.plot([1, 2, 3, 4])

#     return
