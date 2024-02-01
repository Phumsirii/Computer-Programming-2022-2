a=input().strip()
b=open(a,'r')
c=[i.strip() for i in b.readlines()]
b.close()
z=input()
if z=='LSTRIP':
    n=len(c[0])
    d=[len(i.lstrip('.')) for i in c]
    e=max(d)
    f=n-e
    g=[i[f::] for i in c]
    for i in g:
        print(i)
elif z=='RSTRIP':
    n=len(c[0])
    d=[len(i.rstrip('.')) for i in c]
    e=max(d)
    g=[i[:e:] for i in c]
    for i in g:
        print(i)
elif z=='STRIP':
    n=len(c[0])
    d=[len(i.rstrip('.')) for i in c]
    e=max(d)
    g=[i[:e:] for i in c]
    h=[len(i.lstrip('.')) for i in g]
    j=max(h)
    k=[i[e-j::] for i in g]
    for i in k:
        print(i)
elif z=='STRIP_ALL':
    b=[]
    for i in range(len(c[0])):
        a=True
        for e in range(len(c)):
            if c[e][i]!='.':
                a=False
                break
        if a:
            b.append(i)
    d=['' for i in range(len(c))]
    for i in range(len(c)):
        for e in range(len(c[0])):
            if not e in b:
                d[i]+=c[i][e]
    for i in d:
        print(i)
else:
    print('Invalid command')