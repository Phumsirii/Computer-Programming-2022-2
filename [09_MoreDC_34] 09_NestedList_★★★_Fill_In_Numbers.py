def pattern1(nrows,ncols):
    a=[]
    for i in range(nrows):
        a.append([])
    for i in range(nrows):
        a[i]=([e+1 for e in range(i*ncols,(i+1)*ncols)])
    return a

def pattern2(nrows,ncols):
    a=[]
    for i in range(nrows):
        a.append([])
    for i in range(nrows*ncols):
        b=i%nrows
        a[b].append(i+1)
    return a

def pattern3(N):
    a=[]
    for i in range(N):
        a.append([])
    i=0
    b=1
    while i<N:
        for e in range(i):
            a[i].append(0)
        while len(a[i])<N:
            a[i].append(b)
            b+=1
        i+=1
    return a

def pattern4(n):
    a=[]
    for i in range(n):
        a.append([0]*(n-1-i))
    o=True
    i=1
    for e in a:
        while len(e)<n:
            e.append(i)
            i+=1
    for i in range(len(a)):
        a[i]=a[i][-1::-1]
    b=[]
    for i in range(n):
        b.append([])
    for i in range(n):
        for e in range(n):
            b[i].append(a[e][i])
    return b 
    
def pattern5(n):
    a=[]
    for i in range(n):
        a.append([0]*i)
    i=1
    o=True
    while o:
        o=False
        for e in a:
            if len(e)<n:
                e.append(i)
                i+=1
                o=True
    return a

def pattern6(n):
    a=[]
    for i in range(n):
        a.append([0]*i)
    i=1
    o=True
    while o:
        o=False
        for e in a:
            if len(e)<n:
                e.append(i)
                i+=1
                o=True
        for e in a[-1::-1]:
            if len(e)<n:
                e.append(i)
                i+=1
                o=True
    return a
    
exec(input().strip())