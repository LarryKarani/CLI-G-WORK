from Usermodel import Users , Comments, users, comments

print('welcome')

print('please signup')

print('enter username ')
username= input()

print('enter password ')
password = input()
         
new_user = Users(username, password)
new_user.user_signup()
print('successfully signed up')

print('please login')

print('enter username')
username= input()

print('enter password')
password = input()

print('successfuly logged in')

print('create comment')

print('please input comment__')
comment = input()
print('author name')
author = input('please input author__')

new_comment = Comments(comment,author)
print(new_comment.create_comment())
print(comments[0])