a=input()
b=a[1:len(a)-1:1]
c=b.split(',')
g=[float(c[0]),float(c[1]),float(c[2])]
d=input()
e=d[1:len(d)-1:1]
f=e.split(',')
h=[float(f[0]),float(f[1]),float(f[2])]
i=[float(c[0])+float(f[0]), float(c[1])+float(f[1]), float(c[2])+float(f[2])]
print(g,'+',h,'=',i)

