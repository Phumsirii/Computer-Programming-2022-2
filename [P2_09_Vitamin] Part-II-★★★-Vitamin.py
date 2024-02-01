n=int(input())
a=[]
for i in range(n):
    b=input().split()
    a.append(b)
c=input().split()
if c[0]=='show':
    for i in a:
        print(' '.join(i))
elif c[0]=='get':
    z=True
    for i in a:
        if i[0]==c[1]:
            print(' '.join(i))
            z=False
    if z:
        print(c[1],'not found')
elif c[0]=='avg':
    s=0
    for i in a:
        s+=float(i[int(c[1])])
    print(round(s/n,4))
elif c[0]=='max':
    d=[]
    for i in a:
        d.append([-float(i[int(c[1])]),i[0]])
    d.sort()
    print(d[0][1],-d[0][0])
elif c[0]=='sort':
    d=[]
    for i in a:
        d.append([float(i[int(c[1])]),i[0]])
    d.sort()
    e=[]
    for i in d:
        e.append(i[1])
    print(' '.join(e))