myDictionary = {"Costa Rica": "San Jose", "Argentina": "Buenos Aires", "Spain": "Madrid"}
#adding a wrong value
myDictionary["Italy"]="Lisboa"
print(myDictionary)
#changing the wrong value
myDictionary["Italy"]="Rome"
print(myDictionary)
#deleting a value
del myDictionary["Spain"]
print(myDictionary)

#multiple types in a dictionary
myDictionary2 = {"Costa Rica": "San Jose", 7:"Cristiano Ronaldo", "Phone Number": 88888888}
print(myDictionary2)

#working with tuples and dictionaries

myTuple = ["Spain", "Costa Rica", "Argentina"]
myDictionary3 = {myTuple[0]: "Madrid", myTuple[1]:"San Jose", myTuple[2]:"Buenos Aires"}
print(myDictionary3)
print(myDictionary3["Spain"])

#assign multiple values to a key

myDictionary4 = {7:"Cristiano Ronaldo", "Team": "Juventus", "Champions": {"Seasons": [2008,2014,2016,2017,2018]}}
print(myDictionary4["Champions"])