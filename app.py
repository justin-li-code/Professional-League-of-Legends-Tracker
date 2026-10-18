import pandas as pd
import streamlit as st

st.title("Pro Pick/Ban Tracker")

df = pd.read_csv("data/your_file.csv", low_memory=False)
patch = st.selectbox("Patch", sorted(df["patch"].dropna().unique()))
d = df[df["patch"] == patch]

picks = d[d["position"] != "team"]["champion"].value_counts().head(10)
st.subheader("Most picked")
st.bar_chart(picks)
