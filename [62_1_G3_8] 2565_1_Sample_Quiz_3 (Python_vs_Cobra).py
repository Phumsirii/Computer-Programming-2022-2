a=int(input())
s={} #k:v=party:votes[Y,N,X]
x={} #k:v=party:agreement
y={} #k:v=party:[cobra]
l=[]
for i in range(a):
    c=input().strip()
    l.append(c)
    s[c]=[0,0,0]
    x[c]=''
    y[c]=set()
b=int(input())
d={} #k:v=sorsor:party
for i in range(b):
    c=input().strip().split()
    d[c[0]]=c[1]
c=int(input())
e={} #sorsor:vote
for i in range(c):
    v=input().strip().split()
    e[v[0]]=v[1]
    if v[1]=='Y':
        s[d[v[0]]][0]+=1
    elif v[1]=='N':
        s[d[v[0]]][1]+=1
    elif v[1]=='X':
        s[d[v[0]]][2]+=1
for i in s:
    q=max(s[i])
    v='YNX'
    if s[i].count(q)==1:
        x[i]=v[s[i].index(q)]
    else:
        x[i]='-'
for i in e:
    w=d[i] #sorsor's party
    if e[i]!=x[w]:
        if x[w]=='-':
            y[w]={'Inconclusive'}
        else:
            y[w]=y[w]|{i}
for i in l:
    print(i)
    k=sorted([e for e in y[i]])
    if len(k)>0:
        print(', '.join(k))
    else:
        if s[i]==[0,0,0]:
            print('Inconclusive')
        else:
            print('No cobra')