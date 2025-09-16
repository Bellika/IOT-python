from config import get_connection

class UserDB:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def to_dict(self):
        return {'username': self.username, 'password': self.password}
    
def load_users_db():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT username, password FROM users")
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    users = [UserDB(row['username'], row['password']) for row in result]
    return users

def save_user_db(user: UserDB):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(sql, (user.username, user.password))
    conn.commit()

    cursor.close()
    conn.close()
    print(f"User {user.username} saved")
