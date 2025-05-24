import streamlit as st
from astro_api import *
from utils import detect_sign_from_date

st.set_page_config(page_title="Astrology Birth Chart GPT", layout="centered")

st.markdown("<h1 style='text-align: center;'>🔮 Astrology Birth Chart GPT</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Expert astrologer GPT that needs your birth info to answer queries.</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,1,1])
with col2:
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Astrology_symbol.svg/2048px-Astrology_symbol.svg.png", width=100)
st.markdown("---")

# Predefined button layout (mimicking your image)
col1, col2 = st.columns(2)
with col1:
    if st.button("What does my birth chart say about me?"):
        st.info(get_birth_chart_placeholder("You", "YYYY-MM-DD", "HH:MM", "City"))

    if st.button("Can you analyze my love life through astrology?"):
        sign = st.selectbox("Select Zodiac Sign", zodiac_signs, key="love")
        st.success(get_love_prediction(sign))

with col2:
    if st.button("Tell me about my career prospects astrologically."):
        sign = st.selectbox("Select Zodiac Sign", zodiac_signs, key="career")
        st.success(get_career_prediction(sign))

    if st.button("Can you describe my main weaknesses?"):
        sign = st.selectbox("Select Zodiac Sign", zodiac_signs, key="weakness")
        st.success(get_weakness_analysis(sign))

st.markdown("---")

st.subheader("📅 Daily Horoscope")
sign = st.selectbox("Your Zodiac Sign", zodiac_signs, key="daily")
if st.button("🔍 Show Horoscope"):
    st.info(get_daily_horoscope(sign))

st.markdown("---")

st.subheader("📜 Generate Your Birth Chart")
with st.form("birth_form"):
    name = st.text_input("Name")
    birth_date = st.date_input("Birth Date")
    birth_time = st.time_input("Birth Time")
    birth_place = st.text_input("Place of Birth")
    submitted = st.form_submit_button("Generate")
    if submitted:
        result = get_birth_chart_placeholder(name, birth_date, birth_time, birth_place)
        st.success(result)
