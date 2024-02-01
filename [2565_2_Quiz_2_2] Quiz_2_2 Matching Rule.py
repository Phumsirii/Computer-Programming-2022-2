def match(s,cs):
    a=[]
    b=[]
    c=[]
    for i in s:
        a.append(i)
    i=0
    while i<len(cs):
        if cs[i]=='[':
            z=cs.find(']')
            b.append(cs[i+1:z])
            c.append(1)
            i=z+1
        elif cs[i]=='(':
            z=cs.find(')')
            b.append(cs[i+1:z])
            c.append(2)
            i=z+1
        elif cs[i]=='?':
            c.append(3)
            b.append('?')
            i+=1
        else:
            b.append(cs[i])
            c.append(0)
            i+=1
    if len(a)!=len(b):
        return False
    for i in range(len(c)):
        if c[i]==0:
            if b[i]!=a[i]:
                return False
        elif c[i]==1:
            if not a[i] in b[i]:
                return False
        elif c[i]==2:
            if a[i] in b[i]:
                return False
    return True
exec(input())