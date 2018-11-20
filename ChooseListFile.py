changedefault1 = input("Default of custom (D) or (C): ")
if changedefault1 == "D":
    txtfilewords = open("listwithwords_1.txt", "wr")
    txtfileanswers = open("listwithanswers_1.txt", "wr")



elif changedefault1 == "C":
    print("Put file in directory with this app")
    filetext = input("Name of file: ") + ".txt"
    txtfile = open(filetext, "wr")


