import numpy as np

def read_data():
    w=[float(e) for e in input().split()]
    weight=np.array(w)
    n=int(input())
    data=np.ndarray((n,4),int)
    for i in range(n):
        data[i]=[int(e) for e in input().split()]
    return weight,data

def report_lower_than_mean(weight,data):
    d=data[::,1::]
    name=data[::,0]
    score=np.sum(d*weight,axis=1)
    mean=sum(score)/data.shape[0]
    lower=list(name[score<mean])
    if len(lower)>0:
        i=[str(e) for e in lower]
        print(', '.join(i))
    else:
        print('None')

exec(input().strip())