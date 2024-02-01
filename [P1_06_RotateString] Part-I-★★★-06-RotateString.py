import random
a=str(input())
b=int(input())
c=0
d=[]
z=0
while c<b:
    e=input()
    d+=[str(e)]
    c+=1
if b>1:
    m=random.randint(0,len(d)-1)
    n=random.randint(0,len(d)-1)
    while m==n:
        m=random.randint(0,len(d)-1)
        n=random.randint(0,len(d)-1)
    if len(d[m])!=len(d[n]):
        print('Invalid size')
        z+=1
    else:
        pass
else:
    pass
if a=='90' and z==0:
    k=[]
    for g in d:
        j=[]
        for i in range(len(g)):
            j+=g[i:i+1:]
        k+=[j]
    l=k[::-1]
    for p in range(len(l[0])):
        t=''
        for q in range(b):
            t+=str(l[q][p])
        print(t)
elif a=='flip'and z==0:
    for a in d:
        print(a[::-1])
elif a=='180'and z==0:
    f=d[::-1]
    for g in f:
        print(g[::-1])