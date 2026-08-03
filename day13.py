# create and access
python=['def','int','for','import','if']
print('first word is',python[0],'\nmiddle word is',python[2],'\nlast word is',python[-1])
subjects = ["math", "physics", "python", "english"]
print('valus in subject except the first and last are',subjects[1:- 1])
# unpack
coords = [12.9, 79.9]
num=[11.7,243,45,78,90,12.9]
first, *middle, last=num
lat, lon=coords
print(lat,lon)
print(middle)
print(first,last)
#explore & analyze
# max value
scores = [45, 89, 100, 10, 90]
j=scores[1]
for i in scores:
      if i >j:
         j=i
print('max',j)
# min value
scores = [45, 89, 23, 67, 10, 91]
j=scores[0]
for i in scores:
      if i <j:
         j=i        
print('min',j)
# scores = [45, 89, 23, 67, 90, 91]
# print(max(scores))
# print(min(scores))
# count
count=0
scores = [45, 89, 23, 67, 90, 91]
for i in scores:
   if i >50:
      count +=1
print(count)
# change
tasks = ["python", "git"]
print(tasks)
tasks.append('prompt engineering')
print(tasks)
tasks.remove('git')
print(tasks)
tasks.insert(0,'python advanced')
print(tasks)
# tricky
a = [1,2,3]
b=a#refers to same obj
b.append(4)
print(a)
# remove duplicates
task = [45, 89, 23, 67, 45, 18]
new=[]
for i in task:
    if i not in new:
        new.append(i)
print(new)
# move zeros to last
scores=[0,1,0,13,45]
insert_pos=0
for i in range(len(scores)):
    if scores[i]!=0:
        scores[insert_pos]=scores[i]
        insert_pos+=1
for i in range(insert_pos,len(scores)):
    scores[i]=0  
print(scores)        
# reverse  the list 
num=[1,2,4,5,6,7]
l=0
r=(len(num)-1)
while l<r:
        num[l],num[r]= num[r],num[l]
        l+=1
        r-=1
print(num)

      