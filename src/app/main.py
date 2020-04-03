import os 
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse
import httpx 

prefix = "/api/v1"

app = FastAPI(
    title="Analytics Pipeline",
    openapi_url=prefix,
    docs_url=f"{prefix}/docs",
    redoc_url=None,
)

@app.get("/pbp/")
def play_by_play(gameId: str):
    key = os.getenv('SR_KEY') 
    url = f"http://api.sportradar.us/nbdl/trial/v7/en/games/{gameId}/pbp.json?api_key={key}" 
    response = httpx.get(url)
    return response.json()

