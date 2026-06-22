# numbers 1 to 15
i=1
while i<=15:
    print(i)
    i+=1
#stop by users
val=0
while val!= "stop":
    print(val)
    val=input("enter name or stop")
   
# sum of odd num
j=1
sum=0
while j<=50:
    if j%2!=0:
       sum+=j  
    j+=1
print(f"sum of odd numbers from 1 to 50 is {sum}") 
# triangle of numbers
for i in range(1,5):
    print(f'{i} ' *i)
# reverse star pattern
for i in range(5,0,-1):
    print(f'* ' *i)
# multiplicaation table
for i in range(1,11):
    for j in range(3,12,3):
        print(f'{i*j}',end='\t')
    print()  
# skip multiples of 4
for i in range(1,21):
    if i %4==0:
        continue
    else:
        print(i)
# variation
sum=0
while True:
    num =int(input('enter the number'))
    if num <0:
        break
    if num==0:
        continue
    sum+=num
print(f'sum of numbers{sum}')
# mix
for i in range(1,31):
    if i%2 ==0 or i%3 ==0:
        continue
    if i%7 ==0 and i%5==0:
        break
    print(f'{i}')    


    





