from fastapi import FastAPI
from src.functional import calculation
from typing import Dict

app = FastAPI()


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello World"}


@app.get('/{s}')
def get_item(s: str) -> float:
    ans = calculation(s)
    if ans == int(ans):
        return int(ans)
    else:
        return ans
