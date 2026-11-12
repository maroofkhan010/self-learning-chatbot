import json
with open("full_forms01.json",'r') as file: 
    data=json.load(file)
print("HOW TO USE THE CHATBOT")  
print("STEP1:what is (anything for full forms)") 
print("STEP2:step1 is the format for talking with the chatbot")
print("STEP3:if chatbot has not the answer you can teach him")
print("STEP4:follows chatbot command") 
print("\n")
while True:
    user_input=input("YOU:")
    if "what is" in user_input or "hi" in user_input or "how" in user_input or "who" in user_input:
    
     if user_input in data:
        print("BOT:",data[user_input])
     else:  
        print("BOT:sorry, i do not have this one.") 
        teach=input(" can you teach me  answer yes/no: ").strip().lower()    
        if teach=='yes':
            ans=input("BOT:please enter the full form: ").strip().lower()
            data[user_input]=ans
            with open("full_forms01.json",'w') as file:
                json.dump(data,file,indent=4)
            print("BOT:Thanks, Added Succesfully")    
        elif teach=='no':
              print("BOT:No problem") 
        else:
            print("BOT:please respond in the form of yes or no")    
            teach=input(" can you teach me  answer yes/no: ").strip().lower()    
            if teach=='yes':   
              ans=input("BOT:please enter the full form: ").strip().lower()
              data[user_input]=ans
              with open("full_forms01.json",'w') as file:
                json.dump(full_forms01,file,indent=4)
              print("BOT:Thanks, Added Succesfully")    
    else:
       print("enter a valid one")         
        



