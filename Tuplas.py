#tuples

firstTuple=("Carlos",24,9,1991)
print(firstTuple)

#convert tuple to list
firstList=list(firstTuple)
print(firstList)

#convert list to tuple

secondTuple=tuple(firstList)
print(secondTuple)

#find into a tuple
print("Carlos" in firstTuple)
print(firstTuple.count("Carlos"))

#length
print(len(firstTuple))
