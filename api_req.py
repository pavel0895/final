import requests
from config import BASE_URL, API_KEY

def get_current_user(token=API_KEY):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/v1/users/current", headers=headers)
    return response
