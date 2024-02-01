def p(x):
    a=[]
    for i in x:
        a.append(i)
    a.sort()
    b=[]
    for i in a:
        if x[i]>1:
            b.append(['-','remove',str(x[i]),i+"'s"])
        else:
            b.append(['-','remove',str(x[i]),i])
    return b

z=input()
a=z.lower()
y=input()
b=y.lower()
c={}
d={}
for i in a:
    if 'a'<=i<='z':
        if i in c:
            c[i]+=1
        else:
            c[i]=1
for i in b:
    if 'a'<=i<='z':
        if i in d:
            d[i]+=1
        else:
            d[i]=1
e={}
f={}
for i in c:
    if i in d:
        if c[i]>d[i]:
            e[i]=c[i]-d[i]
    else:
        e[i]=c[i]
for i in d:
    if i in c:
        if d[i]>c[i]:
            f[i]=d[i]-c[i]
    else:
        f[i]=d[i]
print(z)
if len(e)>0:
    l=p(e)
    for i in l:
        print(' '.join(i))
else:
    print('-','None')
print(y)
if len(f)>0:
    for i in p(f):
        print(' '.join(i))
else:
    print('-','None')