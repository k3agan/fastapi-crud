from app.api import ping
from app.api import sequence
from fastapi import FastAPI

app = FastAPI()

app.include_router(ping.router)
app.include_router(sequence.router)


# Minimum viable (with just the plotly data stuff) graph for testing


# @app.get("/graph")
# def graph():
#     plt.plot([1, 2, 3, 4])

#     return
