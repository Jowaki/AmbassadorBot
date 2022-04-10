import sys
from chatterbot import ChatBot
import pandas as pd
import string
import StudentDetails as SD


from tkinter import * 

# global res 
# res=""
# global uinput 
# uinput= ""

# root = Tk()

# root.title ('Chat Bot')

# chatWindow = Text(root, bd=1, bg='white', width = 50, height = 0)

# chatWindow.place(x=6, y=6, height = 386, width = 370)


# messageWindow = Text(root, bg='white', width = '30', height = 0 )
# messageWindow.place(x=150, y=400, height = 50, width = 260)



# Button = Button(root, text='Send', bg='blue', activebackground='grey', width=12, height= 5)
# Button.place(x=6, y=400, height = 50, width = 120)

# scrollbar = Scrollbar(root, command = chatWindow.yview())
# scrollbar.place(x=375, y=5, height = 385 )



readfaq = pd.read_excel('school.xlsx', sheet_name = 'FAQ')

question = readfaq['Question'].tolist()
response = readfaq['Response'].tolist()

readconversation = pd.read_excel('school.xlsx', sheet_name = 'Conversation')

greetings = readconversation['Greeting'].tolist()
praisings = readconversation['Praising'].tolist()
endings = readconversation['Ending'].tolist()
cquestions = readconversation['Question'].tolist()
canswers = readconversation['Answer'].tolist()



uinput = " "
res = "Hi,"

def inCquestions():
    global uinput
    for i in range(len(cquestions)):
        if str(cquestions[i]) in uinput:
            print ("Bot: " + canswers[i])
            return True
    return False

def inFAQs():
    global uinput
    global res
    for i in range(len(question)):
        if question[i] in uinput:
            res = response[i]
            print ("Bot:", end = ' ')
            print(*res.split(' . '), sep = '\n        ')
            return True
    return False

def inGreetings():
    global uinput
    global res
           
    for phrase in greetings:
        if str(phrase) in uinput:
            res = str(phrase).capitalize() + ", how may I assist you?"
            print ("Bot: "+ res)
            return True
    return False

def inPraisings():
    global uinput
    global res
    for phrase in praisings:
        if str(phrase) in uinput:
            res = "Thanks a lot, always happy to help"
            print ("Bot: "+ res)
            return True
    return False
            
# def get_input():
#      value=messageWindow.get("1.0","end-1c")
#      return (value)
        
    
    
def  Chatting():
    global res
    global userinput
    while True:
        print()
        
        # Button = Button(root, text='Send',command = lambda:get_input(), bg='blue', activebackground='grey', width=12, height= 5)
        # Button.place(x=6, y=400, height = 50, width = 120)
        
        userinput = input("You: ").lower().translate(str.maketrans('', '', string.punctuation))
       # uinput = Button (command = lambda:get_input())#input("You: ").get_input()
        #uinput = str(get_input()).lower().translate(str.maketrans('', '', string.punctuation))
        if res == "Please enter your admission number":
            if userinput.isdigit():
                if(SD.showdetails(int(userinput))):
                    res = ' '
                continue
            else:
                print("Bot: Wrong admission number. Please enter again.")
                continue
            
        if  any(phrase in userinput for phrase in endings):
            return
            
        if  inCquestions():
            continue
        if inFAQs():
            continue
        if inGreetings():
            continue
        if inPraisings():
            continue

        file = open("questions.txt", 'a')
        file.write(userinput + '\n')
        file.close()
        print ( "Bot: Sorry wasn't able to get that, contact the reception for info regarding that")
       # output.config(text = bot_text);

        
# label = Label( chatWindow, text = "Mark is the chatbot\nBot: Hi, my name is Mark and I'm here to assist you!", )
# label.pack(side =TOP, anchor = NW)
bot_name = "Mark"
print ("Mark is the chatbot\nBot: Hi, my name is Mark and I'm here to assist you!")
# Button = Button(root, text='Send',command = lambda:get_input(), bg='blue', activebackground='grey', width=12, height= 5)
# Button.place(x=6, y=400, height = 50, width = 120)

Chatting()
print ("Bot: Bye, talk to you later. Hope I could help you out")



#root.mainloop()