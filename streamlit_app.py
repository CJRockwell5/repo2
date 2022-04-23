import streamlit as st
bot_chance = st.slider('Chance of Botryis', min_value=0, max_value=100)
sug_high = st.slider('Chance of High Sugar', min_value=0, max_value=100)
sug_med = st.slider('Chance of Medium Sugar', min_value=0, max_value=100)
sug_low = st.slider('Chance of Low Sugar', min_value=0, max_value=100)

if bot_chance*95.2*275000 > (sug_med + sug_high)*95.2*(125000 + 117500):
  st.text(bot_chance)
else:
  st.text(sug_med + sug_high)
