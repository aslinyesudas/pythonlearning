# object = A "bundle" of related attribute (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) use to design the structure and layout of an object

from car import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("corvette", 2025, "blue", True)
car3 = Car("charger", 2026, "yellow", True)

car1.drive()
car1.stop()

