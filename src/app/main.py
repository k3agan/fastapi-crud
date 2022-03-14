from fastapi import FastAPI
from app.db import engine, database, metadata

from app.api import ping
from app.api import sequence

app = FastAPI()

metadata.create_all(engine)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(ping.router)
app.include_router(sequence.router)

# Minimum viable (with just the plotly data stuff) graph for testing

# @app.get("/graph")
# def graph():
#     plt.plot([1, 2, 3, 4])

#     return
