from datetime import datetime

users = []
comments = []
replies = []


class Users():
    counter = 1

    def __init__(self, username, password, isAdmin, isModerator):
        self.id = self.counter
        self.createdAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.username = username
        self.password = password
        self.isAdmin = False
        self.isModerator = False

    def user_signup(self):
        user = {}
        user['id'] = self.id
        user['name'] = self.username
        user['password'] = self.password
        Users.counter += 1

    def log_out_user(self):
        user_logout = False
        return {"message": "successfully logged out"}
