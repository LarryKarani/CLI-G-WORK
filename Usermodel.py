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

    def user_signup(self):
        user= {}
        user['id']=self.id
        user['name']=self.username
        user['password']=self.password
        Users.counter +=1

class Comments(Users):
     count = 1
     def __init__(self,comment,author):
         self.comment = comment
         self.author = author
         self.user_id = self.checkuser(author)

     def create_comment(self):
         comment={}
         comment['id'] = self.id
         comment['description'] = self.comment
         comment['author'] = self.author
         comment['user_id'] = user_id
         Comments.count +=1
         


        