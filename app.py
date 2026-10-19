import pandas as pd
import streamlit as st

st.set_page_config(page_title="Pro Pick/Ban Tracker")
st.title("Pro Pick/Ban Tracker")
st.caption("Data: Oracle's Elixir. Fan project, not endorsed by Riot Games.")

@st.cache_data
def load():
    return pd.read_csv("pro_data.csv", low_memory=False)

df = load()
patches = sorted(df["patch"].dropna().unique())
patch = st.selectbox("Patch", patches, index=len(patches) - 1)

d = df[df["patch"] == patch]
games = d["gameid"].nunique()
st.write(f"{games} games on patch {patch}")

players = d[d["position"] != "team"]
teams = d[d["position"] == "team"]

pick_rate = (players["champion"].value_counts() / games * 100).head(10)
ban_cols = [f"ban{i}" for i in range(1, 6)]
bans = pd.concat([teams[c] for c in ban_cols]).dropna()
ban_rate = (bans.value_counts() / games * 100).head(10)

st.subheader("Top 10 pick rate (% of games)")
st.bar_chart(pick_rate)

st.subheader("Top 10 ban rate (% of games)")
st.bar_chart(ban_rate)
