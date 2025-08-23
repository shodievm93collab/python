# Exception Handling Exercises
# 1 Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
def calc(n):
try:

return 1/n
except ZeroDivisionError:
return &#39;Noldan boshqa son kirit!&#39;
print(calc(2))

# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception
if the input is not a valid integer
def calc(n):
try:
return 1/int(n)
except ValueError:
return &#39;Raqam kirit!&#39;

print(calc(input(&#39;Son kiriting &#39;)))

# 3 Write a Python program that opens a file and handles a FileNotFoundError exception if the file does
not exist.
def calc(n):
try:
with open(n,&#39;r&#39;) as f:
return f.read()
except FileNotFoundError:
return &#39;Fayl topilmadi!&#39;
print(calc(input(&#39;Fayl nomi va joylashgan joyini kiriting &#39;)))

# 4 Write a Python program that prompts the user to input two numbers and raises a TypeError
exception if the inputs are not numerical.
def calc(w1,w2):
try:
for i in (w1,w2):
if i not in (&#39;0123456789&#39;):
1+i
else:

print(&#39;ok&#39;)
except TypeError:
return &#39;Raqam kiritilmagan!&#39;
w1=input(&#39;Raqam kirit &#39;)
w2=input(&#39;Yana raqam kirit &#39;)
print(calc(w1,w2))

# 5. Write a Python program that opens a file and handles a PermissionError exception if there is a
permission issue.
def calc(tx):
try:
with open (tx,&#39;w&#39;) as f:
f.write(&#39;tttaaaa&#39;)
return &#39;OK&#39;
except PermissionError:
return &#39;Fayl ochiq!&#39;
print(calc(input(&#39;Faylni ko`rsat &#39;)))

# 6. Write a Python program that executes an operation on a list and handles an IndexError exception if
the index is out of range.
def calc(t):
try:
a=[1,2,3,4]
return a[t]
except IndexError:
return &#39;Noto`g`ri raqam!&#39;
print(calc(int(input(&#39;Raqam kirit &#39;))))

# 7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt
exception if the user cancels the input.
try:
a=input(&#39;Raqam kirit! &#39;)
print(a)

except KeyboardInterrupt:
print(&#39;Toxtatma&#39;)

# 8. Write a Python program that executes division and handles an ArithmeticError exception if there is
an arithmetic error.
try:
10/0
except ArithmeticError:
print(&#39;Xato&#39;)
# 9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an
encoding issue.
