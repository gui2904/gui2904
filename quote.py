import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_quote():
    try:
        api_key = os.getenv("QUOTES_API")
        api_url = 'https://api.api-ninjas.com/v1/quotes'
        response = requests.get(api_url, headers={'X-Api-Key': api_key})       
        if response.status_code == 200:
            data = response.json()[0]
            return data["quote"], data["author"]
    except Exception as e:
        return f"Could not fetch quote. ({e})", ""

    return "No quote found.", ""
