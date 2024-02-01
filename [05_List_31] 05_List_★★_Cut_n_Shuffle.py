a=input().split()
b=input()
c=[b[n] for n in range(len(b))]
for i in c:
    if i=='C':
        l=int(len(a)/2)
        a1=a[:l:]
        a2=a[l::]
        a=a2+a1
    elif i=='S':
        v=[]
        l=int(len(a)/2)
        for m in range(l):
            v.append(a[m])
            v.append(a[m+l])
        a=v
    else:
        pass
h=' '.join(a)
print(h)