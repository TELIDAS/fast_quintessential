from sqlalchemy import Column, ForeignKey, Integer, String, Float, Index, Enum, BigInteger

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    wallet = relationship("Wallet", back_populates="owner", uselist=False)


class Crypto(Base):
    __tablename__ = "cryptos"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    symbol = Column(String, unique=True, index=True)
    price = Column(BigInteger)


class Wallet(Base):
    __tablename__ = "wallets"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    balance = Column(Float, default=0.0)

    owner = relationship("User", back_populates="wallet")
    transactions = relationship("Transaction", back_populates="wallet")


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    wallet_id = Column(Integer, ForeignKey("wallets.id"))
    crypto_id = Column(Integer, ForeignKey("cryptos.id"))
    amount = Column(Float)
    type = Column(Enum("buy", "sell", name="TransactionType"))

    __table_args__ = (
        Index('ix_transactions_wallet_id_crypto_id', 'wallet_id', 'crypto_id'),
    )
    wallet = relationship("Wallet", back_populates="transactions")
    crypto = relationship("Crypto")
