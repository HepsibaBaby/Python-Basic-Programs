'''thistuple = ("Hepsiba",(1,2,3),[4,5,6])
print(thistuple[2][1])

tuple1 = (100)
print(type(tuple1))

set1 = {1,2,3,4}
set2 = {4,5,6}
set3 = set1.difference(set2)
set4 = set2.difference(set3)
set5 = set3.union(set4)
print(set5)

list1 = [1,2,3,4,5]
s = set(list1)
print(s)

pass_s = {"A","B","C"}
fail_s = {"C"}
students = pass_s - fail_s
print(students)

mystr = input("enter the string")
c=0
for i in mystr:
    if(i=="a"):
        c = c + 1
print(c, "times")

dict = {}
print("empty dictionary:")
print(dict)'''

#Write a program to check whether a given key exist in a dictionary or not
d={1:"Apple",2:"Orange",3:"Grape"}
x = int(input("Enter the value"))
if x in d.keys():
    print("key is exist")
else:
    print("key is not exist")

#Convert two list to dictionary
list1 = [1,2,3]
list2 = ["a","b","c"]
dictionary = dict(zip(list1,list2))
print(dictionary)





