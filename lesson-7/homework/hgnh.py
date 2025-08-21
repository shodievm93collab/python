1. is_prime(n) funksiyasi
def is_prime(n):
for i in range(2,int(n/2)+1):
if n%i==0:
return False
else:
return True
print(is_prime(17))

2. digit_sum(k) funksiyasi
def digit_sum(k):
ls=list(map(int,list(x for x in str(k))))
return sum(ls)
print(digit_sum(502))

3. Ikki sonning darajalari
n=1
while 2**n&lt;10:
print(2**n,end=&quot; &quot;)
n+=1
