a=str(input())
b=[]
for c in range(len(a)):
    b.append(a[c])
d=['0','1','2','3','4','5','6','7','8','9']
for n in b:
    if n in d:
        d.remove(n)
if len(d)>0:
    e=','.join(d)
    print(e)
else:
    print('None')