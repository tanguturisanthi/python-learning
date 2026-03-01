#using replace()
text="+49 (176) 123-4577"
print(text.replace("+","").replace("(","").replace(")","").replace("-","").replace(" ",""))
#string inspector
name=input("enter your lovely name:")
print(len(name))
print(name.count("a"))
print(name.upper())
print(name.lower())
print(len(name.replace(" ","")))
print(name.split(" ")[0])

#name formatter
text=input("enter your full name:")
print(text.upper())
print(text.lower())
print(len(text.replace(" ","")))
print(text[::-1])
print(text.split(" ")[0])
print(text.split(" ")[-1])
