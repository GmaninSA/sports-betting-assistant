import sqlite3
import random
from betting_config import BET_SIZE

def simulate_bet(best_bet):
    conn = sqlite3.connect("sports_betting.db")
    cursor = conn.cursor()

    favorite = best_bet['team_a'] if best_bet['odds_a'] < best_bet['odds_b'] else best_bet['team_b']
    fav_odds = min(best_bet['odds_a'], best_bet['odds_b'])
    won = random.random() < (1 / fav_odds)
    payout = BET_SIZE * (fav_odds - 1) if won else -BET_SIZE

    cursor.execute("SELECT bankroll FROM bets ORDER BY id DESC LIMIT 1")
    last_bankroll = cursor.fetchone()
    bankroll = last_bankroll[0] if last_bankroll else 1000
    bankroll += payout

    cursor.execute("""
    INSERT INTO bets (date, match, favorite, odds, won, payout, bankroll)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        best_bet['date'],
        f"{best_bet['team_a']} vs {best_bet['team_b']}",
        favorite,
        fav_odds,
        won,
        payout,
        bankroll
    ))

    conn.commit()
    conn.close()
