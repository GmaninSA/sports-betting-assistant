import os
from dotenv import load_dotenv

load_dotenv()

ODDS_API_KEY = os.getenv("ODDS_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

BANKROLL_START = 1000
BET_SIZE = 50
SPORTS = ['soccer_epl', 'tennis_atp']
REGION = 'us'
MARKET = 'h2h'
