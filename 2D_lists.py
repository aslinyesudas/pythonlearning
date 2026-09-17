
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "tukey"]

groceries = [fruits, vegetables, meats]


print(groceries[0])

grocery =[["apple", "orange", "banana", "coconut"]
          ["celery", "carrots", "potatoes"]
          ["chicken", "fish", "tukey"]]

for collection in grocery:
    for food in collection:
        print(food, end=" ")
    print()