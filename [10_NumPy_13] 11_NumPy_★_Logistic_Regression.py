import numpy as np
import math

def p(x):
    e=math.e
    return np.array([(1+e**(3.98-0.1*a-0.5*b))**(-1) for a,b in x])
    
exec(input().strip())