# while loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")

while name == "":
    print("you are not enter your name")
    name = input("Enter your name: ")

print(f"Hello {name}")

age = int(input("Enter your age: "))

while age < 0:
    print("Age cant be negative ")
    age = int(input("Enter your age: "))

print(f"you are {age} year old")

food = input("Enter a food you like ( q to quit): ")
while not food == "q":
    print(f"you like {food}")
    food = input("Enter another food you like (q to quit): ")

print("bye")

num = int(input("Enterq a number between 1-10:"))

while num <1 or num >10:
    print(f"{num} is not valid")
    num = int(input("Ente a # betwen 1 - 10: "))

print(f"your number is {num}")
