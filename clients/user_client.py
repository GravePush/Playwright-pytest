import requests


class UserClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_all_users(self):
        return requests.get(url=f"{self.base_url}/users")

    def get_user_by_id(self, user_id: int):
        return requests.get(url=f"{self.base_url}/users/{user_id}")
