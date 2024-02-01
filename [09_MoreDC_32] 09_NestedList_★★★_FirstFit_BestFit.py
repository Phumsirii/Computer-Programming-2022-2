def first_fit(L,e):
    o=True
    for i in range(len(L)):
        if sum(L[i])+e<=100:
            L[i].append(e)
            o=False
            break
    if o:
        L.append([e])
        
def best_fit(L,e):
    a=[]
    for i in range(len(L)):
        if sum(L[i])+e<=100:
            a.append(i)
    b=[]
    for i in a:
        b.append(sum(L[i]))
    if len(b)>0:
        c=max(b)
        L[a[b.index(c)]].append(e)
    else:
        L.append([e])

def partition_FF(D):
    a=[[D[0]]]
    for i in D[1::]:
        o=True
        for e in a:
            if sum(e)+i<=100:
                e.append(i)
                o=False
                break
        if o:
            a.append([i])
    return a

def partition_BF(D):
    a=[]
    for i in D:
        best_fit(a,i)
    return a
    
exec(input().strip())