a=input().split()
spno={}
while a[0]!='END':
    spno[a[0]]=int(a[1])
    a=input().split()
a=input().split()
s={} #{sport:[[faculty,players,{name}]]}
for i in spno:
    s[i]=[]
while a[0]!='END':
    b=a[2].split(',')
    for i in b:
        c=s[i] #[faculty,player]
        d=[e[0] for e in c] #faculty
        if a[1] in d :
            e=d.index(a[1])
            if not a[0] in s[i][e][2]:
                s[i][e][1]+=1
                s[i][e][2].add(a[0])
        else:
            s[i].append([a[1],1,{a[0]}])
    a=input().split()
for i in s:
    for e in range(len(s[i])):
        w=spno[i]
        q=s[i][e][1]
        s[i][e].append(q//w)
        s[i][e].append(q%w)

u=sorted([i for i in spno])
for i in u:
    q=sorted(s[i])
    a=''
    for e in q:
        if e[3]>0:
            a+=str(e[0])+'('+str(e[3])+','+str(e[4])+')'
    print(i+':'+a)