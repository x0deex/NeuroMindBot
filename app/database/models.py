from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncAttrs
from datetime import datetime
engine = create_async_engine(url="sqlite+aiosqlite:///db.sqlite3",
                             echo=True)

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    balance: Mapped[str] = mapped_column(String(15))


class AiType(Base):
    __tablename__ = "ai_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))

class AiMode(Base):
    __tablename__ = "ai_models"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    ai_type: Mapped[int] = mapped_column(ForeignKey("ai_types.id"))


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(String(50))
    user: Mapped[str] = mapped_column(ForeignKey('users.id'))
    amount: Mapped[str] = mapped_column(String(15))
    create_at: Mapped[datetime]
    order: Mapped[str] = mapped_column(String(100))


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)