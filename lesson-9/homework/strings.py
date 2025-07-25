import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

r = float(input("Enter the radius of the circle: "))
circle = Circle(r)

print(f"Area of the circle: {circle.area():.2f}")
print(f"Perimeter of the circle: {circle.perimeter():.2f}")




from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        
        self.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')

    def get_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

name = input("Enter name: ")
country = input("Enter country: ")
dob = input("Enter date of birth (YYYY-MM-DD): ")

person = Person(name, country, dob)
print(f"{person.name} from {person.country} is {person.get_age()} years old.")





class Calculator:
    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the quotient of a divided by b. Handle division by zero."""
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b

calc = Calculator()

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print(f"Addition: {calc.add(a, b)}")
print(f"Subtraction: {calc.subtract(a, b)}")
print(f"Multiplication: {calc.multiply(a, b)}")
print(f"Division: {calc.divide(a, b)}")





import math

class Shape:
    def area(self):
        """Return the area of the shape."""
        raise NotImplementedError("Subclasses must implement this method.")

    def perimeter(self):
        """Return the perimeter of the shape."""
        raise NotImplementedError("Subclasses must implement this method.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c, height=None):
        self.a = a
        self.b = b
        self.c = c
        self.height = height  

    def area(self):
    
        s = (self.a + self.b + self.c) / 2
        try:
            return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        except ValueError:
            return "Error: Invalid triangle sides."

    def perimeter(self):
        return self.a + self.b + self.c

circle = Circle(5)
square = Square(4)
triangle = Triangle(3, 4, 5)

print("Circle: ")
print(f"  Area: {circle.area():.2f}")
print(f"  Perimeter: {circle.perimeter():.2f}")

print("Square: ")
print(f"  Area: {square.area()}")
print(f"  Perimeter: {square.perimeter()}")

print("Triangle: ")
print(f"  Area: {triangle.area():.2f}")
print(f"  Perimeter: {triangle.perimeter()}")





class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a new value into the BST."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)
        

    def search(self, value):
        """Search for a value in the BST."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        if current is None:
            return False
        if value == current.value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)


bst = BinarySearchTree()
elements = [50, 30, 70, 20, 40, 60, 80]

for elem in elements:
    bst.insert(elem)

search_values = [60, 25, 80]
for val in search_values:
    found = bst.search(val)
    print(f"Value {val} found in BST: {found}")





class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item of the stack."""
        if self.is_empty():
            return "Stack is empty. Cannot pop."
        return self.items.pop()

    def peek(self):
        """Return the top item of the stack without removing it."""
        if self.is_empty():
            return "Stack is empty. Nothing to peek."
        return self.items[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.peek())
print("Popped element:", stack.pop())
print("Top element after pop:", stack.peek())
print("Is stack empty?", stack.is_empty())
print("Stack size:", stack.size())





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None  

    def insert(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, key):
        """Delete the first node with the specified data."""
        current = self.head

        if current is None:
            print("List is empty.")
            return

        if current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"Node with data {key} not found.")
        else:
            prev.next = current.next

    def display(self):
        """Display all the elements in the linked list."""
        if self.head is None:
            print("Linked list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)

print("Linked list after insertion:")
ll.display()

ll.delete(20)
print("Linked list after deleting 20:")
ll.display()

ll.delete(40)  





class ShoppingCart:
    def __init__(self):
        self.items = {}  

    def add_item(self, item_name, price):
        """Add an item to the shopping cart."""
        if item_name in self.items:
            self.items[item_name] += price
        else:
            self.items[item_name] = price

    def remove_item(self, item_name):
        """Remove an item from the shopping cart."""
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Item '{item_name}' not found in cart.")

    def calculate_total(self):
        """Calculate and return the total price of all items."""
        return sum(self.items.values())

    def display_cart(self):
        """Display all items in the cart with prices."""
        if not self.items:
            print("The cart is empty.")
            return
        print("Items in your cart:")
        for item, price in self.items.items():
            print(f"- {item}: ${price:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")


cart = ShoppingCart()
cart.add_item("Apple", 0.99)
cart.add_item("Milk", 2.50)
cart.add_item("Bread", 1.75)

cart.display_cart()

cart.remove_item("Milk")
print("\nAfter removing 'Milk':")
cart.display_cart()







class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Push an item onto the stack."""
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        """Pop the top item off the stack and return it."""
        if self.is_empty():
            print("Stack is empty. Nothing to pop.")
            return None
        item = self.items.pop()
        print(f"Popped: {item}")
        return item

    def display(self):
        """Display all elements in the stack."""
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements (top to bottom):")
            for item in reversed(self.items):
                print(item)

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

stack.pop()
stack.display()

stack.pop()
stack.pop()
stack.pop()  





class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.items.pop(0)
        print(f"Dequeued: {item}")
        return item

    def display(self):
        """Display all elements in the queue."""
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue elements (front to rear):")
            for item in self.items:
                print(item)

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

queue = Queue()

queue.enqueue("Alice")
queue.enqueue("Bob")
queue.enqueue("Charlie")

queue.display()

queue.dequeue()
queue.display()

queue.dequeue()
queue.dequeue()
queue.dequeue()  





class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} to account {self.account_number}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from account {self.account_number}")

    def get_balance(self):
        return self.balance

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: ${self.balance:.2f}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, customer_name, initial_deposit=0):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_number] = BankAccount(account_number, customer_name, initial_deposit)
            print(f"Account created for {customer_name} with account number {account_number}")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def check_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Current balance: ${account.get_balance():.2f}")
        else:
            print("Account not found.")

    def display_customer_info(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            account.display_info()
        else:
            print("Account not found.")



bank = Bank()

bank.create_account("1001", "Alice", 500)
bank.create_account("1002", "Bob", 300)

bank.deposit("1001", 200)
bank.withdraw("1002", 100)

bank.check_balance("1001")
bank.display_customer_info("1002")

bank.withdraw("1002", 1000)
bank.deposit("1003", 50)  

