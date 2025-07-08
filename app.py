import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Daily Sports Betting Dashboard")

# Load your simulation results
df = pd.read_csv("betting_history.csv")

st.subheader("Bankroll Over Time")
fig, ax = plt.subplots()
ax.plot(pd.to_datetime(df['date']), df['bankroll'], marker='o')
ax.set_xlabel("Date")
ax.set_ylabel("Bankroll")
st.pyplot(fig)

st.subheader("Betting History")
st.dataframe(df)
