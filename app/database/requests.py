from app.database.models import async_session
from app.database.models import User
from sqlalchemy import select, delete, desc

def connection(func):
    async def inner(*args, **kwargs):
        async with async_session() as session:
            return await func(session, *args, **kwargs)
    return inner

@connection
async def set_user(session, tg_id):
    user = await session.scalar(select(User).where(User.tg_id == tg_id))

    if not user:
        session.add(User(tg_id = tg_id, balance='0'))
        await session.commit()