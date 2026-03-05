# phone formatted version
phn=input("enter ur number")
print(phn.isnumeric())
print("+91-"+phn[0:5]+"-"+phn[5:10])
print("*****"+phn[5:])
if phn.startswith("98") or phn.startswith("97"):
    print("operator:airtel")
elif phn.startswith("70") or phn.startswith("72"):
    print("operator:jio")
elif phn.startswith("94") or phn.startswith("95"):
    print("operator:vodafone")
else:
    print("unknown operator") 