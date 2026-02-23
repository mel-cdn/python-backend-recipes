from functools import lru_cache

FAKE_USERS_DB = [
    {"id": 1, "name": "Bryce"},
    {"id": 2, "name": "Hernandez"},
    {"id": 3, "name": "Henry"},
]


# 0 - disabled max_size or not using the decorator at all
# None - No limit
@lru_cache(maxsize=None)
def get_users(user_id: int) -> dict | None:
    print(f"> Retrieving user with id {user_id}...")

    return next((user for user in FAKE_USERS_DB if user["id"] == user_id), None)


def main():
    for _id in [1, 2, 1, 3, 3, 3, 2, 1]:
        user = get_users(user_id=_id)
        print(f"id: {user['id']}, name: {user['name']}")


if __name__ == "__main__":
    main()
