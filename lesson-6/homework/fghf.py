6.
1. Modify String with Underscores
def undscor(txt):
    i=2
    while i<len(txt)-1:
        if txt[i].lower() in "aoieu":
            i+=1
        else:
            txt=txt[:i+1]+"_"+txt[i+1:]
            i+=4
    return txt
print(undscor('esreydfsgrt bmgwabt'))

2. Integer Squares Exercise
n=5
for i in range(n):
    print(i**2)

3. Loop-Based Exercises
Exercise 1: Print first 10 natural numbers using a while loop
i=1
while i<=10:
    print(i)
    i+=1

Exercise 2: Print the following pattern
for i in range(1,6):
    for ii in range(1,i+1):
        print(ii, end=" ")
    print("")

Exercise 3: Calculate sum of all numbers from 1 to a given number
try:
    n=int(input("Enter number "))
    result=0
    for i in range(n+1):
        result+=i
    print(f"Sum is: {result}")
except: ValueError

Exercise 4: Print multiplication table of a given number
try:
    n=int(input("Enter number "))
    for i in range(1,11):
        print(n*i)
except: ValueError

Exercise 5: Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in range(len(numbers)):
    try:
        print(numbers[2**i])
    except: IndexError

Exercise 6: Count the total number of digits in a number
try:
    n=int(input())
    print(len(str(n)))
except: ValueError

Exercise 7: Print reverse number pattern
for i in range(5):
    for ii in range(5):
        if 5-i-ii>0:
            print (5-i-ii, end=" ")
    print("")

Exercise 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
for i in range(1,len(list1)+1):
    print(list1[i*-1])

Exercise 9: Display numbers from -10 to -1 using a for loop
for i in range(10):
    print(i-10)

Exercise 10: Display message “Done” after successful loop execution
for i in range(5):
    print(i)
else:
    print("Done")

Exercise 11: Print all prime numbers within a range
for i in range(25,51):
    for ii in range(2,i):
        if i%ii==0:
            break
    else:
        print(i)

Exercise 12: Display Fibonacci series up to 10 terms
for i in range(10):
    if i==0:
        a=0
        b=0
    if i==1:
        a=0
        b=1
    if i==2:
        a=0
        b=1
    c=a+b
    a=b
    b=c
    print(c)

Exercise 13: Find the factorial of a given number
fac=1
for i in range(1,6):
    fac=fac*i
print(fac)

4. Return Uncommon Elements of Lists
list1 = [1, 1, 2]
list2 = [2, 3, 4]
list3=list(filter(lambda x: x not in list2,list1))
list4=list(filter(lambda x: x not in list1,list2))
print(list3+list4)
