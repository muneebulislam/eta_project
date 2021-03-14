"""
A module that tests the databse for the users. It can check the funcionality of creating, updating and deleting
the User infomation in the databse. 
"""
from app.models import User
def test():
    users = {"john":"john@hotmail.com", "kevin": "kevin@hotmail.com", "marry": "marry@gmail.com"}
    for user_name in users:
        db_users = User(username = user_name, email = users[user_name])
        print(db_users.username, db_users.email)
    

    