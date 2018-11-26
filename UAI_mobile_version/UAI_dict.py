#!UAI - User Artificial Intelligence
import random
import time
import pickle #for saving lists
version = "v_2, \"Dictionary\""
wordsdict = {"hello":"Hello", "how are you":"Good, and you?", "version":"Version: "+ version + " made with love"}
with open("worddictiona", "wb") as worddict:
    pickle.dump(wordsdict, worddict)

print(wordsdict)
#HELLO
def hello():
    print("Hello I'm user artificial intelligence")
    uchoose = int(input('''Select mode:
    1.Teach
    2.Talk

    '''))
    return uchoose
#TEACH
def choose_teach():
    print('''Instructions:
    You type a question or dialog
    Then answer on it
    ''')
    print("question: ", end = " ")
    listappend = ["input_there", "input_there_too"]
    listappend[0] = input()
    print("answer: ", end = " ")
    listappend [1] = input()
    return listappend
#TALK
def choose_talk():
	with open("worddictiona", "rb") as worddict:
        	wordsdict = pickle.load(worddict)
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
		for i in wordsdict:
			if userinput == i or userinput.lower() == i:
				print("UAI: " + wordsdict[i])
				complete = 1

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
		wordsdict[listappend2[0]] = listappend2[1]
		print("Learn again? (2 more times): ", end = "") 
		learnq = input("1 - yes, 0 - no: ")
		if learnq == "0":
			with open("worddictiona", "wb") as worddict:
				pickle.dump(wordsdict, worddict)
			break
		elif learnq == "1":
			listappend2 = choose_teach()
			wordsdict[listappend2[0]] = listappend2[1]
			continue
		elif learnq != "1" or learnq != "0":
			while str(learnq) != "1" or str(learnq) != "0":
				print("Try type again: ")
				learnq = input("0/1: ")


	choose_talk()
elif choose == 2:
	choose_talk()

    
