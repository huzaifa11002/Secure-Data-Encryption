import json
import os

users_data = "authentication.json"

def load_user():
    if not os.path.exists(users_data) or os.stat(users_data).st_size == 0:
        return {}
    with open(users_data, "r") as file:
        return json.load(file)

def save_user(user):
    with open(users_data, "w") as file:
        json.dump(user,file, indent=4)

def register_user(username,password):
    users = load_user()
    if username in users:
        return False
    users[username] = {"password":password}
    save_user(users)
    return True

def login_user(username,password):
    users = load_user()
    if username in users and users[username]["password"] == password:
        return True
    return False
