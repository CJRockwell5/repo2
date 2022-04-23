import streamlit as st
bot_chance = st.slider('Chance of Botryis', min_value=0, max_value=100)
sug_high = st.slider('Chance of High Sugar', min_value=0, max_value=100)
sug_med = st.slider('Chance of Medium Sugar', min_value=0, max_value=100)
sug_low = st.slider('Chance of Low Sugar', min_value=0, max_value=100)

if (sug_high + sug_med + sug_low) == 100:
  if bot_chance*95.2*275000 > (sug_med + sug_high)*95.2*(125000 + 117500):
    st.text('Best outcome: Botrytis Mold, chance:')
    st.text(bot_chance)
    if bot_chance*95.2*275000 < (100 - bot_chance)*95.2*35000:
      st.text('Benefits do not outweight downside, harvest now.')
    else:
      st.text('Benefits outweight downside, wait for botrytis mold.')
  else:
    st.text('Best outcome: Medium and High Sugar, chance:')
    st.text(sug_med + sug_high)
    if (sug_med + sug_high)*95.2*(125000 + 117500) < sug_low*95.2*80000:
      st.text('Benefits do not outweight downside, harvest now.')
    else:
      st.text('Benefits outweight downside, wait for additional sweetness.')
else:
  st.text('High, Medium, and Low have to add up to 100')
