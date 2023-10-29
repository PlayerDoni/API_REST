import json
from fastapI import FastAPI, Request, Response
from datetime import datetime

app = FastAPI()

locacoes = []

@app.get("/")
def health_check():
    return {"status" : "ok"}