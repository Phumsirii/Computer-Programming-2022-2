import numpy as np

def toCelsius(f):
    return (f-32)*5/9

def BMI(wh):
    a=[list(i) for i in wh]
    b=[x/((y/100)**2) for x,y in a]
    return np.array(b)

def distanceTo(p,points):
    return np.array([((a-p[0])**2+(b-p[1])**2)**0.5 for a,b in points])

exec(input().strip())