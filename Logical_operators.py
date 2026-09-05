# logical operators = evaluate multiple condition (or, and , not)
#                    or=at least one condition must be True
#                    and= both conditions must be True
#                    not=inverts the condition (not False, not True)

Temp = 25
is_raining = False

if Temp>35 or Temp<0 or is_raining:
    print("The outdoor event is cancelled")

else:
    print("The outdoor event is still scheduled")