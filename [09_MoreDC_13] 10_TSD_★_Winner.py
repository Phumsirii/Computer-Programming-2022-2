n=int(input())
b=set()
w=set()
l=set()
for i in range(n):
    a=input().split()
    c=set(a)
    b=b|c
    w=w|{a[0]}
    l=l|{a[1]}
d=b-l
e=[i for i in d]
print(sorted(e))