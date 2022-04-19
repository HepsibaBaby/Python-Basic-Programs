#Write a program to check whether a person is eligible for voting or not
'''a = int(input("enter your age"))
if a>=18:
    print("Eligible for voting")
else:
    print(("Not eligible for voting"))

#Write a program to check whether the last digit of a number(entered by user) is divisible by 3 or not
num = int(input("enter a number"))
last_digit = num % 10
if last_digit % 3 == 0:
    print("last digit is divisible by 3")
else:
    print("last digit is not divisible by 3")

#write a program to print first 5 odd numbers
for i in range(1, 11, 2):
    print(i)

#Write a program
s = 0
for i in range(10):
    n = int(input("Enter numbers"))
    s = s + n
print(("Avarage of 10 numbers is ", s/10))'''

#Write a program to calculate the electricity bill(accept number of unit from user)
unit = int(input("Enter the number of unit consumed"))
if unit<=100:
    amount = 0
if unit>100 and unit<=200:
    amount = (unit - 100) * 5
if unit>200:
    amount = (unit - 200) * 10
print("Electricity bill: ", amount)

#Write a program to accept percentage from the user and display the grade
mark = float(input("Enter the mark obtained"))
if mark > 90:
    grade = "A"
if mark > 80 and mark<=90:
    grade = "B"
if mark>= 60 and mark<=80:
    grade = "C"
if mark < 60:
    grade = "D"
print("Grade: ", grade)







