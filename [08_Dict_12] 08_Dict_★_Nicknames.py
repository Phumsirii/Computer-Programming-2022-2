n=int(input())
a={}
for i in range(n):
    b=input().split()
    a[b[0]]=b[1]
    a[b[1]]=b[0]
m=int(input())
for i in range(m):
    c=input()
    if c in a:
        print(a[c])
    else:
        print('Not found')