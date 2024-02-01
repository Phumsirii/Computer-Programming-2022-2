def freq(a,b):
    n=0
    for i in a:
        if i==b:
            n+=1
    return n/len(a)

a=int(input())
d={}
for i in range(a):
    b=input()
    c=input().split()
    d[b]=c
e=input()
while e!='-1':
    f={}
    for i in d:
        g=freq(d[i],e)
        h=len(set(d[i]))
        f[g/h]=i
    if len(f)==1 and float(0) in f:
        print('NOT FOUND')
    else:
        print(f[max(f)])
    e=input()