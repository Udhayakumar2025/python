#Reading
file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()

#Read One Line
file = open("sample.txt")

print(file.readline())

file.close()

#Read All Lines
file = open("sample.txt")

for line in file:
    print(line)

file.close()

#Writing
file = open("sample.txt", "w")

file.write("Hello Python")

file.close()

#Appending
file = open("sample.txt", "a")

file.write("\nNew Line")

file.close()