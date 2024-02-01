a=input().split()
b={}
while len(a)==2:
    if not a[0] in b:
        b[a[0]]=set()
    if not a[1] in b:
        b[a[1]]=set()
    b[a[0]].add(a[1])
    b[a[1]].add(a[0])
    a=input().split()
c=a[0]
d={c}
for i in b:
    if c in b[i]:
        d.add(i)
    if i==c:
        d=d|b[i]
for e in d:
    if e in b:
        d=d|b[e]
    for i in b:
        if e in b[i]:
            d.add(i)
e=sorted(list(d))
for i in e:
    print(i)