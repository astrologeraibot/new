import requests

BASE_URL = "https://aztro.sameerkumar.website"  # Free Astro API via POST

zodiac_signs = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

def get_daily_horoscope(sign):
    try:
        res = requests.post(BASE_URL, params={"sign": sign, "day": "today"})
        return res.json().get("description", "No data available.")
    except Exception as e:
        return f"Error: {str(e)}"

def get_love_prediction(sign):
    return f"❤️ {sign}: Your love stars are aligning! Open your heart to connection."

def get_marriage_prediction(sign):
    return f"💍 {sign}: Long-term stability looks promising. A good time for commitments."

def get_career_prediction(sign):
    return f"💼 {sign}: Keep pushing ahead. Career growth is on the horizon."

def get_weakness_analysis(sign):
    return f"🌀 {sign}: Reflect on impulsive behavior and avoid overthinking today."

def get_birth_chart_placeholder(name, date, time, place):
    return f"📜 {name}'s Birth Chart\nDate: {date}, Time: {time}, Place: {place}\n(This is a placeholder. Upgrade to full astrology API for detailed planets & houses.)"
