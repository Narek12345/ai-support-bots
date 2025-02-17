from dotenv import load_dotenv

load_dotenv()



class Config:
	TELEGRAM_BOT_TOKEN = getenv('TELEGRAM_BOT_TOKEN')



config = Config()
