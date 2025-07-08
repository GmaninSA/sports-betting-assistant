import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

st.title("📊 Betting Dashboard")

conn = sqlite3.connect("sports_betting.db")
df = pd.read_sql("SELECT * FROM bets", conn)
conn.close()

st.subheader("Bankroll Over Time")
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

fig, ax = plt.subplots()
ax.plot(df['date'], df['bankroll'], marker='o')
ax.set_xlabel("Date")
ax.set_ylabel("Bankroll")
st.pyplot(fig)

st.subheader("Betting History")
st.dataframe(df)
