import os

from celery import Celery
import httpx

RABBIT_BROKER_URL = os.getenv("RABBIT_BROKER_URL")
celery_app = Celery('tasks', broker=RABBIT_BROKER_URL)


@celery_app.task
def fetch_coin_data():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethereum&order=market_cap_desc&per_page=100&page=1&price_change_percentage=24h"
    response = httpx.get(url)
    return response.json()
