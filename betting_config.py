import streamlit as st

ODDS_API_KEY = st.secrets["ODDS_API_KEY"]
TELEGRAM_BOT_TOKEN = st.secrets["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = st.secrets["TELEGRAM_CHAT_ID"]

BANKROLL_START = 1000
BET_SIZE = 50
SPORTS = ['soccer_epl', 'tennis_atp']
REGION = 'us'
MARKET = 'h2h'
