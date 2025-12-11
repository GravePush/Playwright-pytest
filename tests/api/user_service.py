import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_user(user_id: int):
    r = requests.get(f"https://api.example.com/users/{user_id}")
    return r.json()


def get_all_users():
    response = requests.get(f"{BASE_URL}/users")
    data = response.json()
    return data
