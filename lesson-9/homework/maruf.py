1. Circle Class
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Misol
circle = Circle(5)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())
2. Person Class
from datetime import date

class Person:
    def __init__(self, name, country, birth_date):
        self.name = name
        self.country = country
        self.birth_date = birth_date  # format: YYYY-MM-DD

    def get_age(self):
        birth = date.fromisoformat(self.birth_date)
        today = date.today()
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

# Misol
person = Person("Ali", "Uzbekistan", "2000-06-15")
print("Age:", person.get_age())
3. Calculator Class
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"

# Misol
calc = Calculator()
print("Add:", calc.add(5, 3))
print("Divide:", calc.divide(10, 2))
4. Shape and Subclasses
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

# Misol
shapes = [Circle(3), Square(4), Triangle(3, 4, 5)]
for shape in shapes:
    print(type(shape).__name__, "- Area:", shape.area(), ", Perimeter:", shape.perimeter())
5. Binary Search Tree Class
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(root, key):
            if root is None:
                return Node(key)
            if key < root.key:
                root.left = _insert(root.left, key)
            else:
                root.right = _insert(root.right, key)
            return root

        self.root = _insert(self.root, key)

    def search(self, key):
        def _search(root, key):
            if root is None or root.key == key:
                return root
            if key < root.key:
                return _search(root.left, key)
            return _search(root.right, key)

        return _search(self.root, key)

# Misol
bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
print("Found:" if bst.search(15) else "Not found")
6. Stack Data Structure
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

# Misol
s = Stack()
s.push(1)
s.push(2)
print("Pop:", s.pop())
7. Linked List Data Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Misol
ll = LinkedList()
ll.insert(3)
ll.insert(2)
ll.insert(1)
ll.display()
ll.delete(2)
ll.display()
8. Shopping Cart Class
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = self.items.get(item, 0) + price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(self.items.values())

# Misol
cart = ShoppingCart()
cart.add_item("Apple", 2.5)
cart.add_item("Banana", 1.5)
print("Total:", cart.total_price())
cart.remove_item("Apple")
print("Total after removal:", cart.total_price())
9. Stack with Display
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def display(self):
        print("Stack:", self.stack)

# Misol
s = Stack()
s.push(10)
s.push(20)
s.display()
s.pop()
s.display()
10. Queue Data Structure
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def display(self):
        print("Queue:", self.queue)

# Misol
q = Queue()
q.enqueue(5)
q.enqueue(10)
q.display()
q.dequeue()
q.display()
11. Bank Class
class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name):
        if name not in self.accounts:
            self.accounts[name] = Account(name)

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name].deposit(amount)

    def withdraw(self, name, amount):
        if name in self.accounts:
            return self.accounts[name].withdraw(amount)
        return False

    def get_balance(self, name):
        if name in self.accounts:
            return self.accounts[name].balance
        return None

# Misol
bank = Bank()
bank.create_account("Ali")
bank.deposit("Ali", 1000)
bank.withdraw("Ali", 200)
print("Balance:", bank.get_balance("Ali"))
