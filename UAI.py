#!UAI - User Artificial Intelligence
import random
import time
import pickle #for saving lists
words = ["hello", "how are you", "bye", "who are you", "version"]
answer = ["Hello", "Good, and you?", "bye", "User Artificial Intelligence", "version: 1, UAI, coded with love"]
with open("wordlist", "wb") as wordlistvar:
    pickle.dump(words, wordlistvar)

with open("answerlist", "wb") as answerlist:
    pickle.dump(answer, answerlist)
print(words)

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
    listappend = [0 , 1]
    listappend[0] = input()
    print("answer: ", end = " ")
    listappend [1] = input()
    return listappend
    

def choose_talk():
    with open("wordlist", "rb") as wordlistvar:
        words = pickle.load(wordlistvar)

    with open("answerlist", "rb") as answerlist:
        answer = pickle.load(answerlist)
    
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
        for i in range(len(words)):
            if userinput == words[i] or userinput.lower() == words[i]:
                print("UAI: " + answer[i])
                complete = 1

            elif userinput == "exit":
                with open("wordlist", "wb") as wordlistvar:
                    pickle.dump(words, wordlistvar)
                with open("answerlist", "wb") as answerlist:
                    pickle.dump(answer, answerlist)

                UAIexit = "0" 
                break

        if complete == 0:
            print("I don't know what about you talking")

choose = hello()
if choose == 1:
    listappend2 = choose_teach()
    learnq = "1"
    while learnq == 1:

        words.append(listappend2[0])
        answer.append(listappend2[1])
        print("Learn again? (2 more times): ", end = "") 
        learnq = input("1 - yes, 0 - no: ")
        if learnq == "0":
            break
        while learnq != "0" or learnq != "1":
            print("Try type again: ")
            learnq = input("0/1: ")
        


    choose_talk()
elif choose == 2:
    choose_talk()



