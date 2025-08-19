5.
## 1 Leap year
def year_chek(yil):
    return (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0)
yil=int(input("Yilni kiriting "))
if not isinstance(yil, int):
    raise ValueError("Year must be an integer.")
print(year_chek(yil))

2. Conditional Statements Exercise
def n_chek(n):
    if n%2==1:
        return 'Wired'
    elif n>=2 and n<=5:
        return 'Not Wired'
    elif n>=6 and n<=20:
        return 'Wired'
    else:
        return 'Not wired'

n=int(input("Son kiriting "))
if not isinstance(n, int):
    raise ValueError("Son must be an integer.")
print(n_chek(n))

## 3
a=7
b=17
ls=[]
def fin(a,b):
    if a%2==0:
        ls.append(a)
    a=a+1
    if a<b:
        fin(a,b)
    return ls
print(fin(a,b))
