#variables
x=10
y="Hepsiba"
print(x)
print(y)

#Data type
a=5
b="Jasmin"
c=2.5
print(type(a))
print(type(b))
print(type(c))

#List  - store multiple values
mylist = [1,2,3,"Apple","Rose"]
print(mylist)

mylist1=[1,2,3,"Apple","Rose",3,"Rose"]
print(mylist1)  #list allow duplicate values

mylist2=[1,2,"Apple",3,4,"orange","Rose"]
print(mylist2[0])
print(mylist2[1])
print(mylist2[2])   #indexing
print(mylist2[-1])
print(mylist2[-2])  #negative indexing

mylist3 = [1,10,25,50]
mylist3[0]=2
print(mylist3) #change the item of a list using index number
mylist3.append(100)
print(mylist3)  #append an item to the list. The item will add end of the list
mylist3.insert(2,250)
print(mylist3) #insert an item to the list. The item will insert at the specified index

#Tuple
tuple = (1,2,3,4,5)
print(tuple)

#Set - Sets are used to store multiple items in a single variable.Set is unindexed
set1 = {1,2,3,4,5}
set2 = {1,2,3,"a","b"}
print(set1)
set3 = set1.union(set2)
print(set3)
set4 = set1.difference(set2)
print(set4)
set5 = set1.intersection(set2)
print(set5)

#Arithmetic Operations
p=10
q=5
print(p+q)
print(p-q)
print(p*q)
print(p/q)
print(p%q)














