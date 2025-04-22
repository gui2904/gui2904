import datetime
from zoneinfo import ZoneInfo
from greeting import get_greeting
from quote import get_quote

# Get current Eastern time
now = datetime.datetime.now(ZoneInfo("America/New_York"))

quote, author = get_quote()

# Write to README.md
with open("README.md", "w") as f:
    f.write(get_greeting(now))
    f.write(f"📅 Last updated: {now.strftime('%Y-%m-%d %I:%M %p %Z')}\n\n")

    f.write("## 🧠 Quote of the Day\n")
    f.write(f"> *{quote}*\n")
    if author:
        f.write(f"> — {author}\n")

    f.write("\n\n> This README is updated daily via GitHub Actions.\n")
