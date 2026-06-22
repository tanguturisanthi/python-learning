# token counter
msgs=["what is todaay's update","what is claude101?","","this is vscode","tell about vibe coding"]
msgs=["hello world", ""]
count=0
for msg in msgs:
    words=msg.split()
    if msg == "":
       continue
    count+=len(words)
    print(f"words={count}")
    
#  blocked keyword filter
blocked_words=['error','theft','drugs','abuse']
prompt='the theft was happened because theif was using drugs'
words =prompt.split()
for word in words:
    if word in blocked_words:
        print(f"blocked word {word} present")
        break
# chat history formatter
msgs=[{'role':'asst','content':'what is api'},{'role':'user','content':''},{'role':'asst','content':'what is lam'}]
for msg in msgs:
       if msg['content']=='':
        continue
       print(f" role:{msg['role']},content:{msg['content']}")
   

    
     