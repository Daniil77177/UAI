#!UAI - User Artificial Intelligence
import time
import pickle #for saving lists
with open("maindictiona", "rb") as questionanswer:
    maindicti = pickle.load(questionanswer)
print(maindicti)

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
    print("question: ", end = " ")
    questiondef = input()
    print("answer: ", end = " ")
    answerdef = input()
    listappend = [questiondef, answerdef]
    return listappend
    

def choose_talk():
    with open("maindictiona", "rb") as questionanswer:
        maindicti = pickle.load(questionanswer)

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
    while UAIexit == "1":
        complete = 0
        userinput = input("You: ")
        for i in maindicti:
        
            if userinput == i or userinput.lower() == i:
                print("UAI: " + maindicti[i])
                complete = 1
                continue

            elif userinput == "exit":
                complete = 1
                UAIexit = "0" 
                break

        if complete == 0:
            print("I don't know what about you talking")

#Main program

choose = hello()
if choose == 1:

    learnq = "1"
    while learnq == "1":
        listappend2 = choose_teach()
        maindicti[listappend2[0]] = listappend2[1]
        print("Learn again? (2 more times): ", end = "") 
        learnq = input("1 - yes, 0 - no: ")
        if learnq == "0":
            with open("maindictiona", "wb") as questionanswer:
                    pickle.dump(maindicti, questionanswer)
            break
        elif learnq == "1":
            listappend2 = choose_teach()
            maindicti[listappend2[0]] = listappend2[1]
            continue
        while int(learnq) != 1 or learnq != 0:
            print("Try type again: ")
            learnq = input("0/1: ")
            print(learnq)
            print(type(learnq))
        


    choose_talk()
elif choose == 2:
    choose_talk()



