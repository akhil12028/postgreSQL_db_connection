from user import User
from database import Database

Database.initialise(database="learning", user="postgres", password="akhil", host="localhost")

user = User('akhil12028@gmail.com ', 'Akhil', 'Gudavalli')

user.save_to_db()

user_from_db = User.load_from_db_by_email('akhil12028@gmail.com')

print(user_from_db.first_name)
