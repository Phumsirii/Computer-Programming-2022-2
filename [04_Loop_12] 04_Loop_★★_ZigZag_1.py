n=int(input())
x=[]
y=[]
for i in range(n):
    a=input().split()
    x+=[a[0]]
    y+=[a[1]]
m=input()
if m=='Zig-Zag':
    x1=x[::2]
    y1=y[1::2]
    s1=x1+y1
    q=[int(e) for e in s1]
    x2=x[1::2]
    y2=y[::2]
    s2=x2+y2
    w=[int(e) for e in s2]
    print(min(q),max(w))
elif m=='Zag-Zig':
    x1=x[::2]
    y1=y[1::2]
    s1=x1+y1
    q=[int(e) for e in s1]
    x2=x[1::2]
    y2=y[::2]
    s2=x2+y2
    w=[int(e) for e in s2]
    print(min(w),max(q))