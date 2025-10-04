# Week3- Activity 1: Work with .txt file
#Using the demo text file, open, read, and write the complete information for the demo.txt. 


with open("demo.txt",encoding="utf-8", errors="replace") as data:
    lines = data.readlines() # Get a list of all the lines in the file

print("Content")
for line in lines:
    print(line.strip())


with open("output.txt", "w", encoding="utf-8") as data:
    data.writelines(lines)