def mensaje():
  print("Primer acercamiento a funciones en Python")

mensaje()

def suma(num1, num2):
  resultado=num1+num2
  return resultado

res1 = suma(5,7)
print(res1)

res2 = suma(7,7)
print(res2)

res3=suma(9,7)
print(res3)

#arrays

firstList=["Carlos","Jaime","Indira","Juan"]

firstList.append("Marco")

firstList.insert(2,"Juancho")

firstList.extend(["Jorge","Ana","Lucia"])

firstList.extend([1, 21.0, True, False])
print(firstList[:])

firstList.pop()

print(firstList[:])
print(firstList[1:2])
print(firstList[2:])
print(firstList.index("Carlos"))

