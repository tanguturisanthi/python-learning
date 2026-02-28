#type of the data
age=19
food="pizza" 
d=None
minor=False
a=[1.4,"what",23]
t=(1.45,"who",2666)
temp=37.4
print(type(age),type(food),type(d),type(minor),type(a),type(temp),type(t),sep="\n")
#shop bill
item="denver"
quantity=250
price=257.89
stock=True
print(f'{item} of {quantity} ml at price of {price} is available :{stock}')
print(len(item),quantity.bit_length(),sep="\n")
#datatype converter
data=input("enter the value:")
print(data,type(data))
integer=int(data)
print(integer,type(integer))
flow=float(integer)
print(flow,type(float))



