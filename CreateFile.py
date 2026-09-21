import os

os.makedirs("knowledge2", exist_ok=True)
file_path = ("knowledge2\\newfile.txt")

with open(file_path, "x") as file:
    file.write("This is a new file created in the knowledge2 directory.\n")
    file.write("It demonstrates file creation and writing in Python.\n")

with open(file_path, "r") as file:
    contents = file.read()
    print(contents)    
    
file.close()    
 