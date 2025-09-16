import json
import os 

DATA_FILE = os.path.join(os.path.dirname(__file__), '../data/users.json')

class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def to_dict(self):
        return {'username': self.username, 'password': self.password}
    
def load_users():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)
    
    
def save_user(user: User):
    users = load_users()
    users.append(user.to_dict())
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)
