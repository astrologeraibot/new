def detect_sign_from_date(month, day):
    signs = [
        ("Capricorn", 1, 20), ("Aquarius", 2, 19), ("Pisces", 3, 20),
        ("Aries", 4, 20), ("Taurus", 5, 21), ("Gemini", 6, 21),
        ("Cancer", 7, 23), ("Leo", 8, 23), ("Virgo", 9, 23),
        ("Libra", 10, 23), ("Scorpio", 11, 22), ("Sagittarius", 12, 21),
        ("Capricorn", 12, 31)
    ]
    for sign, m, d in signs:
        if (month == m and day <= d) or (month < m):
            return sign
    return "Capricorn"
