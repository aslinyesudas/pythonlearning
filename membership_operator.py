# Membership operator = used to test whether a value or variable if found in a sequence
#                       (string, list, tuple, or dictionary)
#                       1. in
#                       2. not in

word = "APPLE"

letter = input("Guess a letter in secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

students = {"Spongebob", "patrick", "sandy"}

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")

grades = {"Sandy" : "A",
          "Squidward" : "B",
          "Spongebob" : "C",
          "Patric" : "D"}

student = input("Enter the name of a student: ")

if student in gardes:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")