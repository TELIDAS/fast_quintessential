from pydantic import BaseModel
from typing import List

from sqlalchemy import Enum


class CryptoBase(BaseModel):
    name: str
    symbol: str


class CryptoCreate(CryptoBase):
    pass


class Crypto(CryptoBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    wallet: "Wallet"

    class Config:
        orm_mode = True


class WalletBase(BaseModel):
    balance: float


class WalletCreate(WalletBase):
    pass


class Wallet(WalletBase):
    id: int
    transactions: List["Transaction"] = []

    class Config:
        orm_mode = True


class TransactionType(str, Enum):
    buy = "buy"
    sell = "sell"


class TransactionBase(BaseModel):
    amount: float
    type: TransactionType


class TransactionCreate(TransactionBase):
    crypto_id: int


class Transaction(TransactionBase):
    id: int
    wallet_id: int
    crypto_id: int

    class Config:
        orm_mode = True


class CurrencyRequest(BaseModel):
    currency: str
