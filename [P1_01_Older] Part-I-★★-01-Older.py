a=input()
b=input()
c=a.split()
d=b.split()
if c[1]=='January':
    c[1]=1
elif c[1]=='February':
    c[1]=2
elif c[1]=='March':
    c[1]=3
elif c[1]=='April':
    c[1]=4
elif c[1]=='May':
    c[1]=5
elif c[1]=='June':
    c[1]=6
elif c[1]=='July':
    c[1]=7
elif c[1]=='August':
    c[1]=8
elif c[1]=='September':
    c[1]=9
elif c[1]=='October':
    c[1]=10
elif c[1]=='November':
    c[1]=11
elif c[1]=='December':
    c[1]=12
if d[1]=='January':
    d[1]=1
elif d[1]=='February':
    d[1]=2
elif d[1]=='March':
    d[1]=3
elif d[1]=='April':
    d[1]=4
elif d[1]=='May':
    d[1]=5
elif d[1]=='June':
    d[1]=6
elif d[1]=='July':
    d[1]=7
elif d[1]=='August':
    d[1]=8
elif d[1]=='September':
    d[1]=9
elif d[1]=='October':
    d[1]=10
elif d[1]=='November':
    d[1]=11
elif d[1]=='December':
    d[1]=12
e=[int(c[3]),int(c[1]),int(c[2][:-1:1])]
f=[int(d[3]),int(d[1]),int(d[2][:-1:1])]
if e>f:
    print(d[0])
elif e<f:
    print(c[0])
else:
    print(c[0],d[0])