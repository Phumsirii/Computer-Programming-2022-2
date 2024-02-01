def read_matrix():
    m=[]
    nrows=int(input())
    for k in range(nrows):
        x=input().split()
        r=[]
        for e in x:
            r.append(float(e))
        m.append(r)
    return m

def mult_c(c,A):
    for i in range(len(A)):
        for e in range(len(A[i])):
            A[i][e]*=c
    return A 

def mult(A,B):
    c=[]
    for i in range(len(A)):
        d=[]
        for e in range(len(B[0])):
            s=0
            for y in range(len(A[0])):
                s+=A[i][y]*B[y][e]
            d.append(s)
        c.append(d)
    return c
    
exec(input().strip())