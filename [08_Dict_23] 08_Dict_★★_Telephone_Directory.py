n=int(input())
c={}
for i in range(n):
    a=input().split()
    b=a[-1]
    d=' '.join(a[0:-1:1])
    c[b]=d
    c[d]=b
    
m=int(input())
for i in range(m):
    f=str(input())
    if f in c:
        print(f,'-->',c[f])
    else:
        print(f,'-->','Not found')