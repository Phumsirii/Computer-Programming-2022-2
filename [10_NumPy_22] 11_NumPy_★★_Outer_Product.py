import numpy as np

def mult_table(nr,nc):
    a=np.arange(1,nc+1).reshape((1,nc))
    b=np.arange(1,nr+1).reshape((nr,1))
    return a*b

exec(input().strip()) 