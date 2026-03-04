#username generator
name=input("enter your fullname:")
birth_year=input("enter your birth year:")
print(f'enter the username:{name.lower().replace(" ","")+birth_year[2:]}')
#text cleaner
name=input("enter a messy sentence :")
simple_form=name.strip()
print(simple_form)
print(name.lower())
parts=simple_form.split()
print(len(parts))
print(simple_form.startswith("hello"))
print(simple_form.endswith("."))
# Email validator
email=input("enter your email:")
print("@"in email)
print(email.endswith(".com"))
username,domain=email.split("@")
print(f'username:{username}')
print(f'domain part:{domain}')
print(len(email))
# secret code generator
word=input("enter any word:")
secret=word[::-1]
print(secret.upper().replace("A","*").replace("E","*").replace("I","*").replace("O","*").replace("U","*"))
#sentence analyzer
text=input("enter a sentence:")
print(len(text.replace(" ","")))
words=text.split()
print(len(words))
print("python" in text)
print(f'{text}...{text}...{text}')
