from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def pong():
    return {"ping": "pong!"}


@app.get("/sequence")
def pong():
    return {"sequence": ["pong!0", "pong!1", "pong!2"]}

# Minimum viable (with just the plotly data stuff) graph for testing


# @app.get("/graph")
# def graph():
#     plt.plot([1, 2, 3, 4])

#     return
