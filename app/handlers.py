import os
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import F, Router, types

from .keyboards import (create_reply_keyboard, create_inline_keyboard)

router = Router()

@router.message(CommandStart()) 
async def cmd_start(message: Message): 
	await message.answer('Hello, it\'s my first test bot \n Here\'s list of commands\n /help \n /learn', reply_markup=create_reply_keyboard())

@router.message(Command('help'))
async def cmd_help(message:Message):
	await message.answer('command "help"')

@router.message(F.text.lower() == 'pepe')
async def pepe(message: Message):
	with open(os.path.join('app','list.txt'), mode='r') as file:
		await message.answer(file.read(), reply_markup=types.ReplyKeyboardRemove())

#@router.message()
#async def echo(message: types.Message):
#	await message.answer(text=f'{message.text}')

@router.message(F.text == '/learn')
async def cmd_learn(message: Message):
	await message.answer('List of resources:', reply_markup=create_inline_keyboard())