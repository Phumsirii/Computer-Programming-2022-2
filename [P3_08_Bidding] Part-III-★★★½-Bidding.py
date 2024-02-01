n=int(input())
b={}
d=set()
for i in range(n):
    a=input().split()
    d=d|{a[1]}
    if a[0]=='B':
        if a[2] in b:
            c=[e[1] for e in b[a[2]]]
            if a[1] in c:
                z=c.index(a[1])
                b[a[2]].remove(b[a[2]][z])
            b[a[2]].append((int(a[3]),a[1]))
        else:
            b[a[2]]=[(int(a[3]),a[1])]
    elif a[0]=='W':
        if a[2] in b:
            c=[i[1] for i in b[a[2]]]
            if a[1] in c:
                b[a[2]].remove(b[a[2]][c.index(a[1])])
price={}
items={}
for i in d:
    price[i]=0
    items[i]=[]
for i in b:
    if not b[i]==[]:
        e=b[i]
        f=max(e)[0]
        for g in e:
            if g[0]==f:
                price[g[1]]+=f
                items[g[1]].append(i)
                break
y=[i for i in price]
y.sort()
for i in y:
    if price[i]==0:
        print(i+':','$'+str(price[i]))
    else:
        x=' '.join(sorted(items[i]))
        print(i+':','$'+str(price[i]),'->',x)