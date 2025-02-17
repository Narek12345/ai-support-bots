from aiogram import Bot, Dispatcher

from telegram_bot.config import config


bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()
