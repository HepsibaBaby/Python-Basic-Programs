# Write a program for creating(Writing) a file if it doesn't exist
f = open("story.txt", "a")
f.write("Hello world")
f.close()

# Write a program to read entire content of a file
f = open("story.txt", "r")
d = f.read()
print(d)
