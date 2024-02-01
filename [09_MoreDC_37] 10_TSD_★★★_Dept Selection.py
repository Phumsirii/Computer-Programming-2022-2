n=int(input())
b={}
for i in range(n):
    a=input().strip().split()
    b[a[0].strip()]=int(a[1].strip())
n=int(input())
c=[]
for i in range(n):
    a=input().strip().split()
    c.append([float(a[1])]+[a[0]]+a[2::])
c=sorted(c)[-1::-1]
d=[]
for i in c:
    for e in i[2::]:
        if b[e]>0:
            b[e]-=1
            d.append([i[1],e])
            break
for i in sorted(d):
    print(' '.join(i))