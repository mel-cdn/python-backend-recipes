from functools import lru_cache

FAKE_USERS_DB = [
    {"id": 1, "name": "Bryce"},
    {"id": 2, "name": "Hernandez"},
    {"id": 3, "name": "Henry"},
]


# 0 - disabled max_size or not using the decorator at all
# None - No limit
@lru_cache(maxsize=2)
def get_users(user_id: int) -> dict | None:
    print(f"> Retrieving user with id {user_id}...")

    return next((user for user in FAKE_USERS_DB if user["id"] == user_id), None)


# cache slots = [#1] [#2]


def main():
    # SLOT#1 = 1, SLOT#2 = ''
    user = get_users(user_id=1)
    print(f"id: {user['id']}, name: {user['name']}")

    # SLOT#1 = 1, SLOT#2 = 2
    user = get_users(user_id=2)
    print(f"id: {user['id']}, name: {user['name']}")

    # SLOT#1 = 1, SLOT#2 = 2
    user = get_users(user_id=1)  # Should NOT call the gateway and use slot#1 with user_id=1
    print(f"id: {user['id']}, name: {user['name']}")

    # SLOT#1 = 1, SLOT#2 = 2
    user = get_users(user_id=2)  # Should NOT call the gateway and use slot#2 with user_id=2
    print(f"id: {user['id']}, name: {user['name']}")

    # SLOT#1 = 3, SLOT#2 = 2
    user = get_users(user_id=3)  # Replace: slot#1 with user_id=3, because it's the LEAST USED
    print(f"id: {user['id']}, name: {user['name']}")

    # SLOT#1 = 3, SLOT#2 = 1
    user = get_users(user_id=1)  # Will call gateway since slot#1 is replaced with user_id=3
    print(f"id: {user['id']}, name: {user['name']}")

    # SLOT#1 = 3, SLOT#2 = 1
    user = get_users(user_id=3)  # Should NOT call the gateway and use slot#1 with user_id=3
    print(f"id: {user['id']}, name: {user['name']}")

    # SLOT#1 = 3, SLOT#2 = 1
    user = get_users(user_id=1)  # Should NOT call the gateway and use slot#2 with user_id=1
    print(f"id: {user['id']}, name: {user['name']}")

    # SLOT#1 = 2, SLOT#2 = 1
    user = get_users(user_id=2)  # Should call the gateway and use slot#1 with user_id=2
    print(f"id: {user['id']}, name: {user['name']}")

    # SLOT#1 = 2, SLOT#2 = 3
    user = get_users(user_id=3)  # Should call the gateway and use slot#2 with user_id=3
    print(f"id: {user['id']}, name: {user['name']}")


if __name__ == "__main__":
    main()
