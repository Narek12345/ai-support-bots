from telegram_bot.bot.handlers.start import register_start_router


def register_all_routers(dp):
	register_start_router(dp)
