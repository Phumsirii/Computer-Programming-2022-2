def row_number(t,e):
    for i in t:
        if e in i:
            return t.index(i)

def flatten(t):
    a=[]
    for i in t:
        for e in i :
            if e!=0:
                a.append(e)
    return a

def inversions(a):
    n=0
    for i in range(len(a)):
        for e in range(i,len(a)):
            if a[i]>a[e]:
                n+=1
    return n

def solvable(t):
    a=len(t)
    b=inversions(flatten(t))
    if a%2==1:
        if b%2==0:
            return True
    else:
        c=row_number(t,0)
        if b%2==1:
            if c%2==0:
                return True
        else:
            if c%2==1:
                return True
    return False

exec(input().strip())