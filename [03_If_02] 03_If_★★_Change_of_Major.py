a=input()
b=input()
c=a.split()
d=b.split()
e=c[3::]
f=d[3::]
g=[c[0],d[0]]
if c[2]>'A' or c[3]>'C' or c[4]>'C' :
    g.remove(c[0])
if d[2]>'A' or d[3]>'C' or d[4]>'C':
    g.remove(d[0])
if c[2]=='A' and d[2]=='A' and c[3]<='C' and c[4]<='C' and d[3]<='C' and d[4]<='C' :
    if c[1]>d[1]:
        g.remove(d[0])
    elif c[1]<d[1]:
        g.remove(c[0])
    elif c[1]==d[1]:
        if e>f:
            g.remove(c[0])
        elif e<f:
            g.remove(d[0])
        elif e==f:
            g=g
if len(g)==0:
    print('None')
elif len(g)==1:
    print(g[0])
elif len(g)==2:
    print('Both')