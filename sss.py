import re
text="968-Maria, ( D@t@ Engineer );;27yr  "
print(text.strip()) 

pat=(re.split(r'[,(;)]',text))
parts=(text.replace("@","a").replace("yr","").replace(";","").replace("(","").replace(")",""))
# print(parts)
partz=re.split(r'[-, ]',parts) 
# print(partz)
print("name:",partz[1].lower())
print("role:",pat[2].replace("@","a").lower())
# print("role:",partz[4:6])
print("age:",partz[-3])

messy_string = "968-Maria, ( Data Engineer );; 27y "

# Simple string manipulation
name = messy_string.split('-')[1].split(',')[0].strip()
role = messy_string.split('(')[1].split(')')[0].strip()
age = messy_string.split(';')[-1].strip()

clean_summary = f"{name}, {role}, {age}"
print(clean_summary)
