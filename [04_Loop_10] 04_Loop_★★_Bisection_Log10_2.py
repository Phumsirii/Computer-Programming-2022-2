a=float(input())
b=a
l=0
u=1
n=0
while a//10>0:
    a=a//10
    u+=1
    n+=1
x=(l+u)/2
while abs(10**x-b)>(1e-10)*max(b,10**x):
    if 10**x>b:
        u=x
    if 10**x<b:
        l=x
    x=(l+u)/2
print(round(x,6))