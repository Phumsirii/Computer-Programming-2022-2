n=int(input())
a={}
z=[]
for i in range(n):
    b=input().strip().split(':')
    c=b[1].strip().split(', ')
    a[b[0]]=c
    z.append(b[0])
b=input().strip()
c=[]
for i in z:
    for e in a[b]:
        if e in a[i] and not i in c and b!=i:
            c.append(i)
if len(c)==0:
    print('Not Found')
else:
    for i in c:
        print(i)