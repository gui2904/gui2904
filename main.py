import datetime
from greeting import get_greeting
from quote import get_quote

now = datetime.datetime.now(datetime.UTC)
greeting = get_greeting()
quote, author = get_quote()

with open("README.md", "w") as f:
    f.write(f"# 👋 Welcome to my GitHub Profile\n\n")
    f.write(f"## {greeting}\n")
    f.write(f"📅 Last updated: {now.strftime('%Y-%m-%d %H:%M:%S UTC')}\n\n")

    f.write(f"## 🧠 Quote of the Day\n")
    f.write(f"> *{quote}*\n")
    if author:
        f.write(f"> — {author}\n")

    f.write(f"\n\n> This README is updated daily via GitHub Actions.\n")
