from fastapi import FastAPI
from src.functional import calculation

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/{s}')
def get_item(s: str):
    return calculation(s)
