import unittest
from Usermodel import Users, users, comments,replies, Comments, 

class TestUser(unittest.TestCase):

    def test_user_signup(self):
        new_user = Users('larry', 'pass')
        response = new_user.user_signup()

        self.assertTrue(response== 'user created successfully')
    
    def test_create_commets(self):  
        new_user = Users('larry', 'pass')  
        new_user.user_signup()     
        new_comment = Comments('hey you', 'larry')
        response = new_comment.create_comment()
        print(response)
        self.assertTrue(response== 'comment successfully created')
