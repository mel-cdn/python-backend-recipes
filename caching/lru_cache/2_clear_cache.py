import time
from functools import lru_cache
from typing import List

FAKE_USERS_DB = [{"id": 1, "name": "Bryce"}, {"id": 2, "name": "Hernandez"}]


@lru_cache
def get_users() -> List[dict]:
    print("> Retrieving users from a fake gateway...")
    time.sleep(2)
    return FAKE_USERS_DB


def main():
    users = get_users()  # Call 1st time
    print(f"Saving {len(users)} users to file...")

    get_users.cache_clear()  # Clears cache

    # Should call again since cached is cleared
    users = get_users()
    print(f"Saving {len(users)} users to database...")


if __name__ == "__main__":
    main()
