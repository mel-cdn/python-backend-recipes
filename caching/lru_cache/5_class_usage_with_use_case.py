import json
from functools import lru_cache
from typing import List

from caching.lru_cache import reset_database


class CubaoGateway:
    def __init__(self):
        self.database_name = "database.json"

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


class SyncUserUseCase:
    def __init__(self):
        self.gateway = CubaoGateway()

    def execute(self) -> None:
        users = self.fetch_all_users()
        print(users)

        self.gateway.update_user(user_id=1, name="Jaypee")

        # Will still print "Bryce"
        users = self.fetch_all_users()
        print(users)

        # Will print "Jaypee"
        users = self.gateway.fetch_users()
        print(users)

    @lru_cache
    def fetch_all_users(self) -> List[dict]:
        print("> Fetching all users...")
        return self.gateway.fetch_users()


def main():
    uc = SyncUserUseCase()
    uc.execute()


if __name__ == "__main__":
    main()
    reset_database()
