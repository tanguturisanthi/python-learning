# check randomk number is even or not
import random
x=random.randint(1,100)
print(x)
if x%2==0:
    print("x is even")
else:
     print("x is odd") 
#simple calculator
a,b=map(int,input("enter two numbers:").split())
op=input("enter operator:")
res=None
if op == "+":
    res=a+b
elif op == "-":
    res=a-b
elif op =="*":
    res=a*b
elif op =="/":
    if b==0:
        print("can't divide with zero")
    else:
        res=a/b
else:
    print("operator is not valid")   
if res is not None:
    print("result:",res)       
#random number game
import random
x=random.randint(1,100)
y=int(input("guess the number between 1 to 100:"))
if y>x:
    print ("guess is high")
elif y<x:
    print("guess is too low")
else:
    print("guess is correct")
#bill splitter
bill=float(input("enter bill amount"))
tip_percentage=float(input("enter tip percentage"))
people=int(input("enter number of people"))
amount=((tip_percentage/100)*bill)+bill
person_share=amount/people
print("each person share is:",round(person_share,2))
# BMI calculator
wt=float(input("enter weight in kgs"))
ht=float(input("enter height in cms"))
height=ht/100
bmi=wt/(height**2)
print("BMI is ",round(bmi,1))
if bmi<18.5:
  print("underweight")
elif 18.5<=bmi<=24.9:
  print("normal")
elif 25<=bmi<=29.9:
  print("overweight")
else:
  print("obese")
# savings tracker
income=float(input("enter the monthly income"))
rent=int(input("money to pay for the rent "))
food=int(input("money needed for the food "))
electric=int(input("money to pay for the electricity"))
fun=int(input("money needed for the entertainment"))
transport=int(input("money needed for the transportation  "))
total_expenses=rent+food+electric+fun+transport
savings=income-total_expenses
savings_percentage=(savings/income)*100
print("total expenses for a month is",total_expenses)
print("savings for a month is",savings)
print("savings percentage for a month is",round(savings_percentage,1))