# Match-case statement (switch) : An alternative to using many 'elif' statements
#                                 Execute some code if a value matches a 'case'
#                                 Benefits: cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case 1:
            return "Its Sunday"
        case 2:
            return "Its Monday"
        case 3:
            return "Its Tuesday"
        case 4:
            return "Its Wednesday"
        case 5:
            return "Its Thursday"
        case 6:
            return "Its Friday"
        case 7:
            return "Its Saturday"
        case _:
            return "Not a valid day"

print(day_of_week(1))
        


   