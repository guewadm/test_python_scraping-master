# Exercice : 3

# function calculate that takes a list of strings a returns the sum of the list items that represents an integer (skipping the other items).


def calculate(numList):
       if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(calculate([4,3,-2]))

