import json
from functools import lru_cache
from typing import List

from caching.lru_cache import reset_database


class CubaoGateway:
    def __init__(self):
        self.database_name = "database.json"

    @lru_cache
    def fetch_users(self) -> List[dict]:
        print("> Reading from database.json...")
        with open(self.database_name, "r") as f:
            return json.load(f)

    def update_user(self, user_id: int, name: str) -> None:
        print(f"> Updating user with id {user_id}...")
        with open(self.database_name, "r") as f:
            users = json.load(f)

        user = next(u for u in users if u["id"] == user_id)
        user["name"] = name

        with open(self.database_name, "w") as f:
            json.dump(users, f)


def main():
    print("Creating CubaoGateway...")
    gateway = CubaoGateway()

    users = gateway.fetch_users()  # Cached users
    print(users)

    gateway.update_user(user_id=1, name="Jaypee")  # Update user_id=1

    # Will use the cached value "Bryce", which is WRONG!
    # We expected it to be "Jaypee"
    updated_users = gateway.fetch_users()

    print(updated_users)


if __name__ == "__main__":
    main()
    reset_database()
