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

class Moderator(Comments):
    def delete_comment(self,id):
        user = Comments.self.check_comment(id)
        if user:
            comments.remove(user)
        return 'Comment deleted successfully'


    def edit_single_comment(self,id):
        user = Comments.self.check_user(id)
        if user:
            com = Comments.self.check_comment(id)
            if com: 
                com.comment = 'comment'
                return 'edited successfully'
                  
              
class Admin(Moderator):
    def delete_comment(self,id):
        user = Comments.self.check_comment(id)
        if user:
            comments.remove(user)
        return 'Comment deleted successfully'

    def edit_comment(self,id):
        com = Comments.self.check_comment(id)
        if com: 
            com.comment = 'comment'
            return 'edited successfully'
