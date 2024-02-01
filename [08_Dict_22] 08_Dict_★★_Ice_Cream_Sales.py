def reverse(d):
    a={}
    for i in d:
        a[d[i]]=i
    return a
n=int(input())
a={}
for i in range(n):
    b=input().split()
    a[b[0]]=float(b[1])
m=int(input())
s=0
d={}
for i in range(m):
    c=input().split()
    if c[0] in d:
        d[c[0]]+=(int(c[1])*a[c[0]])
        s+=(int(c[1])*a[c[0]])
    elif c[0] in a:
        d[c[0]]=(int(c[1])*a[c[0]])
        s+=(int(c[1])*a[c[0]])

if s>0:
    e=reverse(d)
    f=max(e)
    g=[]
    for i in d:
        if d[i]==f:
            g.append(i)
    g.sort()
    h=', '.join(g)
    print('Total ice cream sales:',str(float(s)))
    print('Top sales:',h)
else:
    print('No ice cream sales')