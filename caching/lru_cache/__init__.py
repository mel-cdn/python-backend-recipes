import json


def reset_database():
    with open("database.json", "r") as f:
        users = json.load(f)
    users[0]["name"] = "Bryce"

    with open("database.json", "w") as f:
        json.dump(users, f)
