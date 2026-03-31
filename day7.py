# # check username and age
# username=input("enter username:")
# age=int(input("enter age"))
# print(username == "")
# print(age>=18)
# # password checker
# pwd=input("enter password")
# print (len(pwd)>=8 and not " " in pwd)
# # email checker
# email=input("enter your email")
# print(email is not ""and "@" in email and email.endswith('.com'))
# # username checker
# user_name=input("enter username")
# print(isinstance(user_name,str) and user_name is not None and len(user_name)>5)
# verify email
role=input("enter role of the user(admin/moderator)")
banned=input("is the user banned or not")
verified=input("user's email is verified or not")
not_banned=banned=='no'
user= role == 'admin' or role== 'moderator'
verified_email=verified=='yes'
print(user and(not_banned or verified_email))

