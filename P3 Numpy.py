import numpy as np

def eq(a,b,p):
    c=1
    for i in a.shape:
        c*=i
    d=a==b
    return np.sum(d)>=c*(p/100)

def closest_point_indexes(points,p):
    a=(points-p)**2
    b=np.sum(a,axis=1)
    c=np.arange(a.shape[0])
    d=np.min(b)
    return c[d==b]

def number_of_inversions(A):
    A=list(A)
    n=0
    for i in range(len(A)):
        for e in range(i,len(A)):
            if A[i]>A[e]:
                n+=1
    return n