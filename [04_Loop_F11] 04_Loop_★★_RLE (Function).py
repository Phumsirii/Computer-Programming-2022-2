def RLE(t):
    if len(t)>0:
        r=str(t[0])
        for i in range(1,len(t)):
            if t[i] != t[i-1]:
                r+=' '
            r+=t[i]
        a=r.split()
        c=[[]]*len(a)
        for b in range(len(a)):
            c[b]=[str(a[b])[0],len(a[b])]
    else:
        c=[]
    return c
exec(input())