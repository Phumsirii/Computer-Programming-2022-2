a=input()
b=[]
c=[]
while a != 'Zig-Zag' and a!='Zag-Zig':
    d=a.split()
    b+=[int(d[0])]
    c+=[int(d[1])]
    a=input()
if a=='Zig-Zag':
    e=b[::2]
    f=c[1::2]
    g=e+f
    h=b[1::2]
    i=c[::2]
    j=h+i
    print(min(g),max(j))
if a=='Zag-Zig':
    e=b[1::2]
    f=c[::2]
    g=e+f
    h=b[::2]
    i=c[1::2]
    j=h+i
    print(min(g),max(j))