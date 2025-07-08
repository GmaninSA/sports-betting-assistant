import sqlite3

conn = sqlite3.connect("sports_betting.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS odds (
    match_id TEXT PRIMARY KEY,
    date TEXT,
    sport TEXT,
    team_a TEXT,
    team_b TEXT,
    draw_option BOOLEAN,
    odds_a REAL,
    odds_b REAL,
    odds_draw REAL,
    true_spread REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS bets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    match TEXT,
    favorite TEXT,
    odds REAL,
    won BOOLEAN,
    payout REAL,
    bankroll REAL
)
""")

conn.commit()
conn.close()
