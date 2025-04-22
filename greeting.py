def get_time(hour):
    if hour < 12:
        return "☀️ Good morning!"
    elif hour < 18:
        return "🌤️ Good afternoon!"
    else:
        return "🌙 Good evening!"


def get_greeting(now):
    greet = f"# 👋 Hey! Welcome to my GitHub Profile\n\n"
    return greet + f"## {get_time(now.hour)}\n"
