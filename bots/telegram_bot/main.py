import os
import sys
import asyncio
from pathlib import Path

def setup_paths():
    """Устанавливаем правильные пути для импортов."""
    current_dir = os.getcwd()
    sys.path.append(current_dir)
    
    parent_dir = str(Path(current_dir).parent.absolute())
    sys.path.append(parent_dir)

setup_paths()

from telegram_bot.bot.create_bot import bot, dp
from telegram_bot.bot.handlers import register_all_routers

register_all_routers(dp)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
