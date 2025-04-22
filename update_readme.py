import datetime

with open("README.md", "w") as f:
    f.write(f"# 📅 Auto-updated README\n")
    f.write(f"Last updated: {datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
    f.write(f"\n> This README is updated daily via GitHub Actions.\n")

