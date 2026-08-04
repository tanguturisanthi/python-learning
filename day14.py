# copy 2 lists
import copy
a=[1,32,5]
b=copy.deepcopy(a)
b.append(99)
print(a,b,sep='\n')
# combine lists
new=['a','v']
n=['d','g']
print(new+n)
n.extend(new)
print(n)
# descending order
# u=[1,67,54,0,19,578]
# n=len(u)
# for i in range(n):
#     for k in range(n-1):   
#          if u[i]>u[k]:
#               u[i],u[k]=u[k],u[i]         
# print('descending order:',u)  
#ascending order
s=[23,89,0,12,87]
num=len(s)
for i in range(num):
     for j in range(num-1):
          if s[j]>s[j+1]:
               s[j],s[j+1]=s[j+1],s[j]
print('ascending order:',s)
#  Descending order
nums = [5, 2, 9, 1, 3]
n = len(nums)
for i in range(n):
    for j in range(n - 1):
        if nums[j] < nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print('descending order',nums) 
# sort lists
w=['santhii','priya','gopikaaa','sam']
c=len(w)
for i in range(c):
     for j in range(c-1):
          if len(w[j]) >len(w[j+1]):
               w[j],w[j+1]= w[j+1],w[j]
print(w) 
# check id  
original=[10,30,59]
new=original.copy()
new.append(68)
print(id(new))
print(id(original))
print(new)
# merge lists
# l1=[1,2]
# l2=[3,4]
# l3=[8,9]
# l4=[]
# for i in range(len(l1)):
#     if l1[i] not in l4:
#         l4.append(l1[i])
# for i in range(len(l2)):        
#     if l2[i] not in l4:
#         l4.append(l2[i])
# for i in range(len(l3)):        
#     if l3[i] not in l4:
#         l4.append(l3[i])
# print(l4)        