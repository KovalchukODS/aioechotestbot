from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import F, Router, types

router = Router()

@router.message(CommandStart()) 
async def cmd_start(message: Message): 
	await message.answer('kchau')

@router.message(Command('help'))
async def cmd_help(message:Message):
	await message.answer('command "help"')


@router.message()
async def echo(message: types.Message):
	await message.answer(text=f'{message.text}')