files = [
    # math_operations.py
    ("math_operations.py", """
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
"""),

    # string_utils.py
    ("string_utils.py", """
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
"""),

    # geometry/__init__.py
    ("geometry/__init__.py", """
from .circle import calculate_area, calculate_circumference
"""),

    # geometry/circle.py
    ("geometry/circle.py", """
import math

def calculate_area(radius):
    return math.pi * radius * radius

def calculate_circumference(radius):
    return 2 * math.pi * radius
"""),

    # file_operations/__init__.py
    ("file_operations/__init__.py", """
from .file_reader import read_file
from .file_writer import write_file
"""),

    # file_operations/file_reader.py
    ("file_operations/file_reader.py", """
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
"""),

    # file_operations/file_writer.py
    ("file_operations/file_writer.py", """
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
""")
]
