import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def check_health():
    return {"status": "OK"}

@app.get("/stress")
async def read_root():
    # Simulate a delay of 5 seconds
    await asyncio.sleep(5)
    return {"message": "Delayed response after 5 seconds"}


# uvicorn app:app --host 0.0.0.0 --port 8000 --reload