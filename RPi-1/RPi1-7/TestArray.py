print("---------------")
print("-- Variables --")
print("---------------")

a = 1
b = 2
c = 3

myList = [a, b, c]

print(myList)
print(a)
print(b)
print(c)

myList[0] = 4

print(myList)
print(a)
print(b)
print(c)

print()
print("-----------")
print("-- Class --")
print("-----------")

class Nummer:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


nummerA = Nummer(1)
nummerB = Nummer(2)
nummerC = Nummer(3)

myClassList = [nummerA, nummerB, nummerC] 

print(myClassList)
print(nummerA)
print(nummerB)
print(nummerC)

myClassList[0].value = 4 
print(nummerA)
print(nummerB)
print(nummerC)
