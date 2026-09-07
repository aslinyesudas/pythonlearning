#collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicate OK
#   Set  = {} unordered and immutable, but Add/Remove OK. NO dupicates
#   Tuple = ()ordered and unchangeable. Duplicates OK. FASTER

#fruits = ["apple", "orange", "coconut", "banana"]
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))

#print("pineapple" in fruits)
#print(fruits[::-1])

#for fruit in fruits:
#    print(fruit)

#fruits[0] = "pineapple"
#fruits.append("pineapple")
#fruits.remove("apple")
#fruits.insert(0, "pinapple")
#fruits.sort()
#fruits.reverse()
#fruits.clear()
#print(fruits.index("apple"))

#print(fruits)

#fruits = {"apple", "orange", "banana", "coconut"}
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("pineapple" in fruits)

#fruits.add("pineapple")
#fruits.remove("apple")
#fruits.pop()
#fruits.clear()

#print(fruits)

fruits = ("apple","banana","pineapple","coconut","orange")
print(fruits.count("coconut"))
