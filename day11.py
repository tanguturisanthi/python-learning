# # duplicate values
# filess=['report.csv','data.xlsx','reporty.csv','data.csv','report.csv','img.jpg']
# seen=[]
# for  file  in  filess:
#     if  file in  seen:
#      print(f"it has duplicate{file}")
#      break
#     seen.append(file) 
# else:
#     print("all are unique ")
# # numbers 1 to 20
# for i in range(1,20):
#    print (f"{i}")
# #even numbers 1 to 20
# print("even numbers from 1 to 20 are")
# for j in range(1,20):
#    if j%2==0:
#       print(f'{j}')
# #  odd numbers 1 to 20 
# print("odd numbers from 1 to 20 are")
# for k in range(1,20):
#    if k%2!=0:
#       print(f'{k}')
# # reverse numbers
# for i in range(20,1,-1):
#    print(f'{i}')
# # 1 to 20 using while
# i=1
# while i <10:
#     print(f'{i}')
#     i+=1
# # asking user to enter 0
# val=int(input("enter the num"))
# while val!=0:
#     print("enter the num again")
#     val=int(input("enter the num"))
# #sum of nums 1 to100
# sum=0
# i=1
# while i in range(100):
#     sum+=i
#     i+=1
# print(f'sum of the numbers from 1 to 100 is{sum}')
# # num of times 3 goes into 100
# money = 100
# count = 0
# while money >= 3:      
#     money -= 3         
#     count += 1         
# print(count)
# # star pattern
# for i in range(1,6):
#      print('* '*i)
# multiplication grid
for i in range(1,6):
    for j in range(1,6):
        print(f"{i*j}",end='\t')
    print()




 
  
    



