def factor(N):
    a=[]
    i=2
    while i<=N:
        if N%i==0:
            b=1
            N/=i
            while N%i==0:
                b+=1
                N/=i
            a.append([i,b])
        i+=1
    return a
exec(input().strip())