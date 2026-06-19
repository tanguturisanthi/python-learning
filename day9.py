# multiplication table
for i in range(1,11):
    val=7*i
    print(f'7*{i}={val}')
#star pattern
for i in  range(7,0,-1):
    print("*"*i)
# list of questions
ques=['what is LLM?','what is RAG?','what is the role of API in LLM app development?','what is a prompt?','what is AI?']
for i,q in enumerate(ques,start=1):
        print(f'{i}. {q}')
# skip empty ones
ques=['what is LLM?','','what is RAG?','what is the role of API in LLM app development?','','what is a prompt?','what is AI?']
for q in ques:
        if not q:
           continue
        print(f'{q}')     
#CHECK API RESPONSES  
API_responses=['success','success','success','error','success','error']
for i,a in enumerate(API_responses,start=1):
       if a=='error':
        print(f'{a} occured at {i}')
        break
# nested loop
que={"sany":['what is ml?','what is vector db?','what is prompting?'],"maki":['what is token?','what is api response?','what is embedding?'],"mai":['what is data engineering?','what is server?','what is backend?']}
for name,ques in que.items():
     print(f"user -{name}")
     for q in ques:
      print(f' -{q}')
 # checks the model
models=['gpt-4','gemini-pro','claude-3','codex','gemini-antigravity']
user=input("enter a model name:")
for m  in models:
       if user == m:
        print("model supported")
        break
else:
   print('model not supported')  
# chat turns
chat_turns= [{"role":"user","content":"what is rag?"},{"role":"asst","content":""},  {"role":"system_error","content":"what is ai"},{"role":"assistant","content":"what is an  app?"}]
count=0
for  chat in chat_turns:
       if chat["role"] =="system_error":
        break
       if chat["content"] =="":
             continue 
       count+=1
                    
       print(f"role:{chat["role"]},content:{chat["content"]}")             
print("valid turns:",count) 
         

