import numpy as np

def peak_indexes(x):
    a=np.arange(1,len(x)-1)
    return a[(x[a]>x[a-1])&(x[a]>x[a+1])]

def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")

exec(input().strip())