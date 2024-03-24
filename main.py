from fastapi import FastAPI
from crypto_app.celery.tasks import fetch_coin_data

app = FastAPI()


@app.get("/fetch-coin-data")
async def trigger_fetch_coin_data():
    data = fetch_coin_data.delay()
    return {"message": "Fetching coin data..."}
