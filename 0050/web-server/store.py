import requests

BASE_URL = "https://api.escuelajs.co/api/v1"

def get_categories():
    r = requests.get(f"{BASE_URL}/categories")
    print(r.status_code)
    print(r.json())
    categories = r.json()
    for category in categories:
        print(category["name"])