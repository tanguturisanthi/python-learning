# #   skip mul of 4
# for i in range(1,21):
#     if i%4==0:
#         continue
#     print(i)
# variation
count=0
while count<3:
    ans=input("enter an answer yes/no")
    count+=1
    if ans== 'yes':
        print("glad we 're on samme page")
        break
    elif count>=3:
        print("we're out of attempts")
#control the attempts while-else 
count=0
while count<3:
    ans=input('enter yes/no')
    if ans=='yes':
        print("glad,we're on same page")
        break
    count+=1
else:
    print("out of tries")    


    
