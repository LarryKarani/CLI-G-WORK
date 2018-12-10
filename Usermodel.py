from datetime import datetime

users = []
comments = []
replies = []


class Users():
    counter = 1

    def __init__(self, username, password, isAdmin, isModerator):
        self.id = Users.counter
        self.createdAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.username = username
        self.password = password
        self.isAdmin = False
        self.isModerator = False
        self.lastloggedIn = None

    def user_signup(self):
        user= {}
        user['id']=self.id
        user['name']=self.username
        user['password']=self.password
        Users.counter +=1

    def check_user(self, username):
        for user in users:
            if user[username]:
                return user
            else:
                return None
        
            
class Comments(Users, author):
     count = 1
     def __init__(self,comment):
         self.comment = comment
         self.id = Comments.count

     def create_comment(self):
         user = check_user(author)
         if not user:
            return 'please login or signup'
         
         comment={}
         comment['id'] = self.id
         comment['comment'] = self.comment
         comment['author'] = user['username']
         Comments.count +=1

    def log_out_user(self):
        return {"message": "successfully logged out"}
       
    def login(self):
        self.lastloggedIn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
