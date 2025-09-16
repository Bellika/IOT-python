from models import User, load_users, save_user, UserDB, load_users_db, save_user_db
from api import fetch_iss_data, save_iss_data, iss_location

if __name__ == '__main__':
    new_user = User(username='John', password='password')
    save_user(new_user)

    load_users()

    iss_iss_data = fetch_iss_data()
    save_iss_data(iss_iss_data)
    print('ISS-data saved')

    new_user_db = UserDB(username='John', password='secret')
    save_user_db(new_user_db)
    all_users_db = load_users_db()

    iss_location()
