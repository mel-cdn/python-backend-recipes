import json
from functools import lru_cache
from typing import List


class CubaoGateway:
    @lru_cache
    def get_users(self) -> List[dict]:
        print("> Reading from database.json...")
        with open("database.json", "r") as f:
            return json.load(f)


def main():
    print("Creating Gateway 1...")
    gateway_1 = CubaoGateway()
    users = gateway_1.get_users()
    print(users)

    users = gateway_1.get_users()
    print(users)

    print("Creating Gateway 2...")
    gateway_2 = CubaoGateway()
    users = gateway_2.get_users()  # should call because this is a different instance
    print(users)


if __name__ == "__main__":
    main()
