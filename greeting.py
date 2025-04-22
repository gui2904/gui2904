import datetime

def get_greeting():
    now = datetime.datetime.now(datetime.UTC)
    hour = now.hour

    if hour < 12:
        return "☀️ Good morning!"
    elif hour < 18:
        return "🌤️ Good afternoon!"
    else:
        return "🌙 Good evening!"
