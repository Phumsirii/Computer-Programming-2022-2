a=input().split()
b=[]
while len(a)==3:
    b.append(a)
    a=input().split()
if a==['1']:
    c={}
    for i in b:
        if i[1] in c:
            c[i[1]]+=int(i[2])
        else:
            c[i[1]]=int(i[2])
    d=sorted((c[i],i) for i in c)[-1:-4:-1]
    e=[b for a,b in d]
    print(', '.join(e))
elif a==['2']:
    c={}
    for i in b:
        if i[1] in c:
            c[i[1]]=c[i[1]]|{i[0]}
        else:
            c[i[1]]={i[0]}
    d=sorted([(len(c[i]),i) for i in c])[-1:-4:-1]
    e=[b for a,b in d]
    print(', '.join(e))
elif a==['3']:
    c={}
    d=set([i[1] for i in b])
    for i in b:
        if i[0] in c:
            x=[h[1] for h in c[i[0]]]
            if i[1] in x:
                c[i[0]][x.index(i[1])][0]-=1
            else:
                c[i[0]].append([-int(i[2]),i[1]])
        else:
            c[i[0]]=[[-int(i[2]),i[1]]]
    e={}
    for i in d:
        e[i]=0
    for i in c:
        f=sorted(c[i])[0][1]
        e[f]+=1
    f=sorted([[e[i],i] for i in e])[-1:-4:-1]
    print(', '.join([b for a,b in f]))