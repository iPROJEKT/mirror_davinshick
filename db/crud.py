from sqlalchemy import select
from aiogram.types import Message

from .base import AsyncSessionLocal
from .model import User


async def get_user(message_data: Message):
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(User).where(
                User.id == message_data.from_user.id
            )
        )
        return result
