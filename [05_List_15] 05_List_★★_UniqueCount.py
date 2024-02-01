a=[int(e) for e in input().split()]
a.sort()
b=[a[0]]
for n in range(len(a)):
    if b[-1]!=a[0]:
        x=a.pop(0)
        b.append(x)
    else:
        a.remove(a[0])
print(len(b))
if len(b)>10:
    print(b[:10:])
else:
    print(b)