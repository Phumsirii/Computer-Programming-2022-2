def reverse(d):
    a={}
    for i in d:
        a[d[i]]=i
    return a

def keys(d,v):
    a=[]
    for i in d:
        if d[i]==v:
            a.append(i)
    return a
exec(input().strip())