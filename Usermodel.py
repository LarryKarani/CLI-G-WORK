from datetime import datetime

users = []
comments = []
replies = []


class Users():
    counter = 1
    def __init__(self, username, password):
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
        user['username']=self.username
        user['password']=self.password
        Users.counter +=1

        users.append(user)

        return 'user created successfully'

               
class Comments(Users):
    count = 1
    def __init__(self,comment,author):
         self.comment = comment
         self.id = Comments.count
         self.author = author

    def create_comment(self):
         comment={}
         comment['id'] = Comments.count
         comment['comment'] = self.comment
         comment['author'] = self.author
         Comments.count +=1
         comments.append(comment)
         
         comments.append(comment)
         return 'comment successfully created'
         
    def log_out_user(self):
        return {"message": "successfully logged out"}
       
    def login(self):
        self.lastloggedIn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
