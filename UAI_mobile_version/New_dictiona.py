import pickle
version = "v_2 , \"Dictionary\""
wordsdict = {"hello":"Hello", "how are you":"Good, and you?", "version":"Version: "+ version + " made with love"}
with open("maindictiona", "wb") as questionanswer:
    pickle.dump(wordsdict, questionanswer)