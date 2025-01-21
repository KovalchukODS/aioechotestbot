import asyncio
from aiogram import Bot, Dispatcher, F

from config import TOKEN
from app.handlers import router


async def main():
	bot = Bot(token=TOKEN)
	dispather = Dispatcher() 
	dispather.include_router(router)
	await dispather.start_polling(bot)

#точка входа в программу
if __name__ == '__main__':
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		print('turning off')