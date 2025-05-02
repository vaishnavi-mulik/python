#Calculator class 
class Calculator:
    def add(self,a,b):
        return a + b

    def subtract(self,a,b):
        return a - b

    def multiply(self,a,b):
        return a * b

    def divide(self,a,b):
        if b == 0:
            return "Cannot divide by zero"
        return a/b

#employee salary calculator
class Employee:
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def give_bonus(self):
        bonus = self.salary*0.10
        self.salary += bonus
        return self.salary

#book class
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discount(self):
        discount = self.price*0.20
        self.price -= discount
        return self.price


#bank account simulation
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited:{amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew:{amount}")
        else:
            print("Insufficient balance for withdrawal.")

    def check_balance(self):
        print(f"Current Balance:{self.balance}")
    

























