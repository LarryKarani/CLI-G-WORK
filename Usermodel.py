from datetime import datetime
users = []
comments = []
replies = []

class Users():
    counter = 1
    
    def __init__(self,username,password,isAdmin,isModerator):
        self.id = self.counter
        self.createdAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.username = username
        self.password = password
        self.isAdmin = False
        self.isModerator = False