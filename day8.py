# login system
username=input("enter username:")
password=input("enter the password")
user_name=username != "" and len(username)>=4
pwd=len(password)>=8 and " " not in password and password not in ("password","12345678")
if bool(username)==user_name and bool(password)==pwd:
    print("login successful")
elif username!=user_name or password!=pwd:
    print("specific error")
# mood router
user=input("enter your present mood like happy or sad or stressed etc..:")
if user== "happy":
    print("Being happyyy is the bestt feeling ever")
elif user=="sad":
    print("it's okay everything will be finee, trust yourself..")
elif user=="stressed":
    print("take a deep breath and think about it with calm mind..")
elif user=="scared":
    print("face your own fears ,there is nothing u gonna lose at the end..")
else:
    print("unknown mood")  
 #  token limit checker 
userr=int(input("enter the number of tokens:"))
if userr<1000:
    print("within limit")
elif 1000<=userr<=1500:
    print("approaching limit")
else:
    print("limit exceeded")
# prompt validator
prompt=input("enter your prompt:")
banned_words=['spam','advertisement','illegal']
if prompt=='':
    print("prompt shouldn't be empty")
elif len(prompt)<10:
    print("prompt is too short")
elif  any(word in prompt for word in banned_words):
    print ("prompt should not have banned words")
else:
    print("prompt accepted")
# model selector
task=input("enter the task type summarize/translate/code/chat:")
budget=input("enter the budget low/high:")
match(task,budget):
     case("summarize","high"):
          print("claude gpt-4,opus")
     case("chat","low"):
          print("haiku")
     case("code","high"):
          print("claude code")
     case("translate","low"):
          print("sonnet4.5")
     case("chat",_):
          print("sonnet4.6") 
     case(_,_):
         print("opus4.3")  
# api response handler
status=int(input("enter the status code 200/400/401/429/500:")) 
retry="yes,retry" if status in(429,500) else"no,retry"
match status:
     case 200:
       print(f"delivered successfully,retry:{retry}")
     case 400:
        print(f"input is wrong ,check  the input;retry:{retry}")              
     case 401:
          print(f"you're not authorized to recieve it;retry:{retry}") 
     case 429:
          print(f"too many requests ,slow down;retry:{retry}")     
     case 500:
            print(f"server crashed wait a little bit;retry:{retry}") 
               