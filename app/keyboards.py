from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)



def create_reply_keyboard() -> ReplyKeyboardMarkup:
	buttons = [
		[KeyboardButton(text='pepe')]
	]
	return ReplyKeyboardMarkup(
		keyboard=buttons,
		resize_keyboard=True
	)

def create_inline_keyboard() -> InlineKeyboardMarkup:
	buttons = [
		[InlineKeyboardButton(text='JS', url='https://uk.javascript.info/')],
		[InlineKeyboardButton(text="AIOgram", url='https://docs.aiogram.dev/uk-ua/latest/')]
	]
	return InlineKeyboardMarkup(
		inline_keyboard=buttons
	)