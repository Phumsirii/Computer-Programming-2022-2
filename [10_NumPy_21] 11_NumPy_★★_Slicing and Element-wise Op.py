import numpy as np

def sum_2_rows(m):
    a=np.ndarray((int(m.shape[0]/2),m.shape[1]),int)
    for i in range(0,len(m),2):
        for e in range(len(m[0])):
            a[i//2][e]=m[i][e]+m[i+1][e]
    return a

def sum_left_right(m):
    n=m.shape[1]//2
    a=m[:,:n:]+m[:,n::]
    return a

def sum_upper_lower(m):
    n=m.shape[0]//2
    return m[:n:,::]+m[n::,::]

def sum_4_quadrants(m):
    n=m.shape[0]//2
    j=m.shape[1]//2
    return m[:n:,:j:]+m[n::,:j:]+m[:n:,j::]+m[n::,j::]

def sum_4_cells(m):
    a=m[::2,::2]
    b=m[::2,1::2]
    c=m[1::2,::2]
    d=m[1::2,1::2]
    return a+b+c+d

def count_leap_years(y):
    y=y[(y-543)%4==0]
    a=y[(y-543)%100==0]
    b=0
    for i in a:
        if (i-543)%400==0:
            b+=1
    return len(y)-len(a)+b

exec(input().strip())