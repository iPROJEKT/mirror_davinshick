from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from db.crud import get_user
from db.const import (
    STRAT_COMAND,
    KEY_SEARCH,
    START_MESSAGE,
    LETS_SEARCH_MESSAGE,
    CREATE_PROFILE
)

router = Router()


@router.message(Command(STRAT_COMAND))
async def start(message: types.Message) -> None:
    if get_user:
        kb = [
            [types.KeyboardButton(text=KEY_SEARCH)],
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
        await message.answer(
            f'{START_MESSAGE}, {message.from_user.first_name}!'
            f'{LETS_SEARCH_MESSAGE}',
            reply_markup=keyboard
        )
    else:
        kb = [
            [types.KeyboardButton(text=CREATE_PROFILE)],
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
        await message.answer(
            f'{CREATE_PROFILE}, {message.from_user.first_name}!',
            reply_markup=keyboard
        )


@router.message(Command(CREATE_PROFILE))
async def create_questionnaire(message: types.Message) -> None:
    pass