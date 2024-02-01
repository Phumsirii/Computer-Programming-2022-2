a=input().lower()
b=input().lower()
c="\"\'/\\,.:; "
d=[]
e=[]
for i in a:
    if not i in c:
        d.append(i.lower())
for i in b:
    if not i in c:
        e.append(i.lower())
d.sort()
e.sort()
if d==e:
    print('YES')
else:
    print('NO')