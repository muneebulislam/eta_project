"""
A module that tests the databse for the users. It can check the funcionality of creating, updating and deleting
the User  and saved Recipe infomation in the databse. 
"""
from app.models import User, Recipe_db
from app import db
def test():
    if User.query.all():  # if User table database is not empty
        db_users = User.query.all()
        for u in db_users:
            db.session.delete(u) # delete all users
    
    

    # dummy data for users.
    users = {"john":"john@hotmail.com", "kevin": "kevin@hotmail.com", "marry": "marry@gmail.com",\
    "crazy":"crazy@gmail.com" }
    for usr in users:
        db_users = User(username = usr, email = users[usr])
        db.session.add(db_users)
    # print the users after insert
    db_users = db.Users.query.all()
    for u in db_users:
        print("username: "+u.username+ "email: "+u.email)


    

    