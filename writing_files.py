# python writing files (.txt, .json, .csv)

txt_data = "I like pizza!"

file_path = "outpust.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")

print()
