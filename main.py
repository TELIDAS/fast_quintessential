from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from crypto_app.database.base import get_db_session

app = FastAPI()

@app.get("/")
async def read_root(db: AsyncSession = Depends(get_db_session)):
    pass