import streamlit as st
bot_chance = st.slider('Chance of Botryis', min_value=0, max_value=100)
sug_high = st.slider('Chance of High Sugar', min_value=0, max_value=100)
sug_med = st.slider('Chance of Medium Sugar', min_value=0, max_value=100)
sug_low = st.slider('Chance of Low Sugar', min_value=0, max_value=100)
st.text(bot_chance)


st.button("Update")
