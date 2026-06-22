sum=0
while True:
    n=int(input("enter a num"))
    if n<0:
        break
    if n==0:
        continue
    sum+=n
print(f'{sum}')    
