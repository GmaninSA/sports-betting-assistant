import streamlit as st

# API keys from Streamlit secrets
ODDS_API_KEY = st.secrets["ODDS_API_KEY"]
TELEGRAM_BOT_TOKEN = st.secrets["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = st.secrets["TELEGRAM_CHAT_ID"]

# Betting parameters
BANKROLL_START = 1000
BET_SIZE = 50

# Sports to track (based on The Odds API sport keys)
SPORTS = [
    'soccer_epl',        # English Premier League
    'tennis_atp',        # ATP Tennis
    'baseball_mlb',      # Major League Baseball
    'americanfootball_nfl',  # NFL Football
    'basketball_nba'     # NBA Basketball
]

# Odds API parameters
REGION = 'us'
MARKET = 'h2h'
