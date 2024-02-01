g=['F','D','D+','C','C+','B','B+','A','A']
a=input()
b=[]
while a!='q':
    b.append(a.split())
    a=input()
b.sort()
c=input().split()
for e in b:
    for d in c:
        if d==e[0]:
            e[1]=g[g.index(e[1])+1]
    print(' '.join(e))