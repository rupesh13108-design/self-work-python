#1. Multiplication Table

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
    


#2. Simple Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)

if num2 != 0:
    print("Division =", num1 / num2)
else:
    print("Division by zero not allowed")


#3. Function Example

def greet(name):
    print("Hello", name)

user_name = input("Enter your name: ")

greet(user_name)


#real problems solving


#1. Student Grade Calculator

name = input("Enter student name: ")
marks = float(input("Enter marks out of 100: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print("\nStudent:", name)
print("Marks:", marks)
print("Grade:", grade)


#2.Electricity Bill Calculator

units = int(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10

print("Total Electricity Bill =", bill)



#3. ATM Withdrawal System

balance = 5000

amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    balance -= amount
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")

    
#4.Bank Account Management System

class BankAccount:

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Current Balance:", self.__balance)


account = BankAccount()

account.deposit(5000)
account.withdraw(2000)
account.show_balance()    



#5.Grocery Expense Tracker

expenses = []

for i in range(5):
    amount = int(input(f"Enter expense {i+1}: "))
    expenses.append(amount)

print("All Expenses:", expenses)
print("Total Expense:", sum(expenses))




# 6. Dog Vaccine Checker

while True:

    dog_name = input("\nEnter dog name: ")
    age = int(input("Enter dog age in weeks: "))

    if age < 6:
        print(dog_name, "is too young for vaccination.")

    elif age < 9:
        print("Vaccine Due: DHPP")
        print("This vaccine helps protect against Distemper, Hepatitis, Parvovirus and Parainfluenza.")

    elif age < 13:
        print("Vaccine Due: DHPP Booster")
        print("This booster dose increases protection against common puppy diseases.")

    else:
        print("Vaccine Due: Rabies")
        print("This vaccine protects against rabies.")

    choice = input("\nDo you want to check another dog? (yes/no): ")

    if choice.lower() != "yes":
        print("Thank you for using Dog Vaccine Checker!")
        break