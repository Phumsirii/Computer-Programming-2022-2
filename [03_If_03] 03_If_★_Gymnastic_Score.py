a=input()
b=a.split()
c=min(b)
d=max(b)
b.remove(c)
b.remove(d)
e=float(b[0])
f=float(b[1])
g=(e+f)/2
print(round(g,2))