from core.fetch_odds import get_combined_odds
from core.select_best_bet import select_best_bet
from core.simulate_bet import simulate_bet
from core.send_alert import send_telegram_alert
import sqlite3

# Fetch and store odds
df = get_combined_odds()
conn = sqlite3.connect("sports_betting.db")
df.to_sql("odds", conn, if_exists="replace", index=False)
conn.close()

# Select best bet
best_bet = select_best_bet(df)

if best_bet is not None:
    simulate_bet(best_bet)
    message = f"🎯 Best Bet: {best_bet['team_a']} vs {best_bet['team_b']} at {min(best_bet['odds_a'], best_bet['odds_b'])} odds\nTrue Spread: {best_bet['true_spread']:.2f}"
    send_telegram_alert(message)
