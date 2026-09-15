def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr", "spongebob", "harold", "squarepants", "III")

def print_address(**kwargs):
    for key, value in kwargs.values():
        print(f"{key}: {value}")

print_address(street="123 fake st.",
              apt="100",
              city="Detroit",
              state="MI",
              zip="54321")