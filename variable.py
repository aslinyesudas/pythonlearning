# Variable = A contaoner for a value (String,Integer,Float,Boolean)
#            A variable behaves as if it was the value it contains
#String
first_name="Bro"
food="Pizza"
email="Bro123@fake.com"
print(f"Hello {first_name}")
print(f"You Like {food}")
print(f"Your email is: {email}")

#Integers
age=25
quantity=3.5
num_of_students=30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} Students")

#Float
price=10.99
gpa=3.2
distance=5.5
print(f"The price is ${price}")
print(f"Your gpa is:{gpa}")
print(f"You ran {distance}km")

#Boolean
is_student=True
for_sale=False
is_online=True
print(f"Are you a student: {is_student}")


if is_student:
    print("You are a student")

else:
    print("You are NOT a student")

if for_sale:
    print("That item is for sale")

else:
    print("That item is NOT available")


if is_online:
    print("You are online")

else:
    print("You are NOT online")