from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from telegram_bot.config import config


bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
