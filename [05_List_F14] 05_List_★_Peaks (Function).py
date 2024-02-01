def peaks(x):
    b=[]
    for a in range(len(x)-1):
        if x[a]>x[a-1] and x[a]>x[a+1]:
            b.append(a)
    return b
exec(input())