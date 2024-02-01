a=float(input())
l=0
u=a
x=(l+u)/2
while abs(10**x-a)>(1e-10)*max(a,10**x):
    if 10**x>a:
        l=l
        u=x
    if 10**x<a:
        l=x
        u=u
    x=(l+u)/2
print(round(x,6))