#split function
'''a = input("enter numbers")
print(a)
print(type(a))
l = a.split(",")
print(l)
for i in range(len(l)):
    l[i]=int(l[i])
print("sum is: ", sum(l))

def diff(a,b):
    difference=a-b
    return difference
d=diff(8,2)
print(d)


#write a python function sum of the all numbers in a list
def sum(numbers):
    total = 0
    for x in numbers:
        total +=x
    return total
print(sum((3,2,3,4,5)))

#Write a lambda function to find square root
square = lambda x:x*x if(x>0) else None
print(square(2))'''

class bank_account:
    def __init__(self):
     self.balance=0
    def account_creation(self):
        self.balance=0
        print("Account created")
    def deposit(self):
        amount=int(input("enter the amount to deposit"))
        self.balance = amount + self.balance
        print("your account balance is: " +str(self.balance))
    def withdraw(self):
        amount=int(input("enter the amount to withdraw"))
        if (self.balance<amount):
            print("insufficient amount")
        else:
            self.balance=self.balance-amount
            print("Your balance amount is:"+str(self.balance))
s=bank_account()
s.account_creation()
s.deposit()
s.withdraw()

