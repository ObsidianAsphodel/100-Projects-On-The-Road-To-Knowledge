import random

randomArray = []
for i in range(15):
    randomArray.append(random.randrange(0,9999))
    print("New element:", randomArray[i])
    print(sorted(randomArray))

unsortedArrayOfStrings = ["Bob", "Phil", "Gracious", "Racous", "Raccoon", "Bear"]

def arrayLength(array):
    for i in range(len(array)):
        return (len(array[i]))
sortedArraysOfStringsWithCount = list(map(arrayLength, unsortedArrayOfStrings))
print(sortedArraysOfStringsWithCount)
print(sorted(unsortedArrayOfStrings))