import requests

def get_quote():
    try:
        response = requests.get("https://api.quotable.io/random", timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data["content"], data["author"]
    except Exception as e:
        return f"Could not fetch quote. ({e})", ""

    return "No quote found.", ""
