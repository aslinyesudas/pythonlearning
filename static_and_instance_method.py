# Static methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general utility funcyions

# Instance method = Best for operations on instance of the class (Objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee :
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name}={self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_position = ["manager", "Cashier", "Cook", "Janitor"]
        return position in valid_position

employee1 = Employee("Eugune", "Manager")
employee2 = Employee("Sqidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")


print(Employee.is_valid_position("Cook"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())