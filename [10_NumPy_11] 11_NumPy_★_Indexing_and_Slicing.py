import numpy as np

def get_column_from_bottom_to_top(a,c):
    b=[]
    for i in a[-1::-1,c]:
        b.append(i)
    return np.array(b)

def get_odd_rows(a):
    return a[1::2,]

def get_even_column_last_row(a):
    return a[-1,0::2]

def get_diagonal1(a):
    b=[list(i) for i in a]
    return np.array([b[e][e] for e in range(len(b))])

def get_diagonal2(a):
    b=[list(i) for i in a]
    return np.array([b[e][-(e+1)] for e in range(len(b))])

exec(input().strip())