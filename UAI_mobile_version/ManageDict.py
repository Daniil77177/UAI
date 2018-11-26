import time
import pickle #for saving lists
program = "on"
while program == "on":
    with open("worddictiona", "rb") as questionanswer:
        maindicti = pickle.load(questionanswer)
    print(maindicti)
    #Now variable "maindicti" is variable where all our value saves


    print("What you wanna do?: ")
    print(
    '''

    1.Save new question and answer
    2.Delete question and answer
    3.Change question and answer

    '''
    )
    what = input("Enter the number: ")

    if what == "1":
        print('''Instructions:
        You type a question or dialog
        Then answer on it
        ''')
        print("question: ", end = " ")
        questiondef = input()
        print("answer: ", end = " ")
        answerdef = input()
        maindicti[questiondef] = answerdef

        with open("worddictiona", "wb") as questionanswer:
            pickle.dump(maindicti, questionanswer)


    if what == "2":
        print(maindicti)
        print("Enter name of question and it will remove from the variable with answer")
        deleteque = input()
        if deleteque in maindicti:
            del maindicti[deleteque]
        else:
            print("Key not find")

    if what == "3":
        print('''
        Change key? Or value?
        ''')
        num = input("1/2: ")
        if num == "1":
            print("Previous name and new name")
            pr = input("Previous name of key: ")
            new_key = maindicti[pr]
            newname = input("New name of key: ")
            del maindicti[pr]
            maindicti[newname] = new_key

        elif num == "2":
            print("Enter name of the key and new value")
            key = input("Key: ")
            value = input("Value: ")
            maindicti[key] = value
    print("Save changes?")
    savechanges = input("Yes / no: ")
    if savechanges.lower() == "yes":
        with open("worddictiona", "wb") as questionanswer:
            pickle.dump(maindicti, questionanswer)
    print("Try again?")
    program = input("yes or no: ")
    if program.lower() == "no" or program.lower() == "n":
        program = "off"
        exit()
    elif program.lower() == "yes" or program.lower() == "y":
        program = "on"



