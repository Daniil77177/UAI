import pickle
with open("maindictiona", "rb") as questionanswer:
    maindicti = pickle.load(questionanswer)
for i in maindicti:
    if "am" in maindicti:
        