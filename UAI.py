import random
import time
words = ["hello", "how are you", "bye", "who are you", "version"]
answer = ["hello", "Good, and you?", "bye", "User Artificial Intelligence", "version: 1, UAI, coded with love"]
def hello():
    print("Hello I'm user artificial intelligence")
    uchoose = int(input('''Select mode:
    1.Teach
    2.Talk 
    '''))
    return uchoose

def choose_teach():
    print('''Instructions:
    You type a question or dialog
    Then answer on it
    ''')


def choose_talk():
    print("Let's talk")
    #time.sleep(2)
    print("Your UAI loading")
    #time.sleep(2)
    print("Start", end ="")
    #time.sleep(2)
    print(".", end ="")
    #time.sleep(2)
    print(".", end ="")
    #time.sleep(2)
    print(".")
    print()
    UAIexit = "1"
    complete = 0
    while UAIexit == "1":
        userinput = input("You: ")
        for i in range(len(words) - 1):
            if userinput == words[i] or userinput.lower() == words[i]:
                print("UAI: " + answer[i])
                complete = 1
            elif userinput == "exit":
                UAIexit = "0" 
                break
        if complete == 0:
            print("I don't know what about you talking")

choose = hello()
if choose == 1:
    choose_teach()
elif choose == 2:
    choose_talk()



