
#Dictionary containing point values for each letter
pointDict = {}
pointDict.update(dict.fromkeys(["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], 1))
pointDict.update(dict.fromkeys(["D", "G"], 2))
pointDict.update(dict.fromkeys(["B", "C", "M", "P"], 3))
pointDict.update(dict.fromkeys(["F", "H", "V", "W", "Y"], 4))
pointDict["K"] = 5
pointDict.update(dict.fromkeys(["J", "X"], 8))
pointDict.update(dict.fromkeys(["Q", "Z"], 10))

word = input("Please enter your word: \n")
sum = 0

for x in word:
        sum += pointDict[x.upper()]

print(sum)
