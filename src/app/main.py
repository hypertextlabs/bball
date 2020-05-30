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

envk = os.getenv('SR_KEY') 
KEY = f"/pbp.json?api_key={envk}"

BASE_URL = 'http://api.sportradar.us/nbdl/trial/v7/en/'
URL_K = 'games/'

# GET Play by play 
@app.get("/playbyplay")
def play_by_play(gameId: str):
    url = f"{BASE_URL}{URL_K}{gameId}{KEY}" 
    response = httpx.get(url)
    return response.json()

# GET Team breakdown
@app.get("/team")
def player_profile(playerId: str):
    url = f"{BASE_URL}{URL_K}{gameId}{KEY}" 
    response = httpx.get(url)
    return response.json()

# GET Player breakdown
@app.get("/player")
def player_profile(playerId: str):
    url = f"{BASE_URL}{URL_K}{gameId}{KEY}" 
    response = httpx.get(url)
    return response.json()
