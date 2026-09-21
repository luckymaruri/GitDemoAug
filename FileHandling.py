# open File
#Relative path knowledge\input.txt
#absolute path C:\Practice\AugustDemo\knowledge\input.txt   
# file = open("knowledge\\input.txt", "r") #open file to read
 
#open file to write - w+ all operations read and write - a+ is for append
file = open("knowledge\\input.txt", "a+")

#write to the file
file.write("This is a test file for file handling in Python.\n")

#close the file
file.close() 

#open file to read
file = open("knowledge\\input.txt", "r")

#store contents in a file variable
contents = file.read()

#close the file
file.close()    

#print the contents of the file
print(contents)
