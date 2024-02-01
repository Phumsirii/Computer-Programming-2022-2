a=int(input())
b=int(input())
if a<=0:
    if b<=0:
        print('Invalid n and k')
    else:
        print('Invalid n')
elif b<=0:
    print('Invalid k')
else:
    c=[str(i+1)+'-'*(a+1-len(str(i+1))) for i in range(b)]
    c[-1]=c[-1][:-1:]
    print(''.join(c))
    f=['0','1']
    for e in range(a-1):
        g=['0'+i for i in f]
        h=['1'+i for i in f[-1::-1]]
        f=g+h
    j=[]
    m=0
    n=b
    while m<len(f):
        j.append(f[m:n])
        m=n
        n+=b
    for i in j:
        print(','.join(i))