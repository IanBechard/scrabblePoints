#Ian Bechard
#28-10-2019


#Dictionary containing point values for each letter
pointDict = {}
pointDict.update(dict.fromkeys(["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], 1))
pointDict.update(dict.fromkeys(["D", "G"], 2))
pointDict.update(dict.fromkeys(["B", "C", "M", "P"], 3))
pointDict.update(dict.fromkeys(["F", "H", "V", "W", "Y"], 4))
pointDict["K"] = 5
pointDict.update(dict.fromkeys(["J", "X"], 8))
pointDict.update(dict.fromkeys(["Q", "Z"], 10))

#If user would like to !quit
nquit = True

while(nquit):
    word = input("Please enter your word: ")
    sum = 0

    #Sum values of each letter
    for x in word:
        sum += pointDict[x.upper()]

    #Ask if double
    dbl = (input("Is it a double word? (y/n): ").upper()  == "Y")
    if(not dbl): #dont ask if triple if its double
        #ask if triple, do calculation if so
        trpl = (input("Is it a triple word? (y/n): ").upper()  == "Y")
        if(trpl):
            sum *= 3

    #calculation for double word
    if(dbl):
        sum *= 2

    #ask for double or triple letters
    dbl = input("Please enter all double letters, Eg. cabbage => bbg, if b, b, g each land on double, blank if no doubles: ")
    trpl = input("Please enter all triple letters, Eg. cabbage => bbg, if b, b, g each land on triple, blank if no triples: ")

    for x in dbl:
        sum += pointDict[x.upper()]

    for x in trpl:
        sum += (2*pointDict[x.upper()])


    print("The total point value of ", word, " is ", sum)

    nquit = (input("Would you like to calculate another words value? (y/n): ").upper() == "Y")
