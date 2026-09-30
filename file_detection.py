# python file detection

import os

file_path = "test.txt"

if os.path.exists(file_path):
    print(f"The locaton '{file_path}' exists")
else:
    print("That location does't exists")