vowels = ["A","a", "E", "e", "I", "i", "O", "o", "U", "u"]
def countVowelsInString (arg):
    vowelsCount = 0
    argArray = list(arg)
    for i in range(len(arg)):
        if ((arg[i] == "a") or (arg[i] == "e") or (arg[i] == "i") or (arg[i] == "o") or (arg[i] == "u") or (arg[i] == "A") or (arg[i] == "E") or (arg[i] == "O") or (arg[i] == "U")):
            vowelsCount += 1
    print (argArray)
    print ("There are", vowelsCount, "vowels in", arg)

countVowelsInString("Gracious")
countVowelsInString("September")
countVowelsInString("Salacious")
countVowelsInString("Gardevoir")
countVowelsInString("Hydreigon")

def countVowelsInStringOptimized(arg):
    vowelCount = 0
    for i in range(len(arg)):
        if arg[i] in vowels:
            vowelCount += 1
    print("There are", vowelCount, "vowels in", arg)

countVowelsInStringOptimized("Given")
countVowelsInStringOptimized("Braggadocious")
countVowelsInStringOptimized("Lenient")
countVowelsInStringOptimized("Rebuttal")
# comparing the array to the parameter passed in 

# list, turns each letter into an element of it's own
# python has Lists, Sets and Tuples, not Arrays?

# 1. Brute Force Approach 
# 2. Refinement

# in - determines whether a given value is present in the given sequence(string, array, list, etc.)
