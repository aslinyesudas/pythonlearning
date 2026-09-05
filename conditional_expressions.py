#conditional exressions = A one-line shortcut for the if-else statement (ternary operator)
#                         print or assign one of two values based on a condition
#                         X if condition else Y

num = 5
a=6
b=7
temparature=20
user_rule="admin"

#print("Positive" if num>0 else "negative")
#result = "Even" if num%2==0 else "odd"
#max_num=a if a > b else b
#min_num=a if a < b else b
#status="Adult" if age>= 18 else "Child"
#weather="Hot" if temparature >20 else "cold"
access_level="Full access" if user_rule=="admin" else "Limited access"

print(access_level)