a=input().split()
b=open(a[0],'r')
c=open(a[1],'r')
d=[]
for e in b:
    g=e.split()
    d.append([g[0][-2::]]+g)
for f in c:
    h=f.split()
    d.append([h[0][-2::]]+h)
b.close()
c.close()
d.sort()
for i in d:
    print(i[1],i[2])