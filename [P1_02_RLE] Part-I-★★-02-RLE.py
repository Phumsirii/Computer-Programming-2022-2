a=input()
if a=='str2RLE':
    b=str(input())
    d=[b[0]]
    e=[1]
    f=1
    for c in range(1,len(b)):
        if b[c]==b[c-1]:
            z=e[f-1]+1
            e[f-1]=z
        elif b[c]!=b[c-1]:
            d+=[b[c]]
            e+=[1]
            f+=1
    g=['']*(2*len(e))
    g[::2]=d
    g[1::2]=[str(i) for i in e]
    h=' '.join(g)
    print(h)
elif a=='RLE2str':
    b=input().split()
    alpha=b[::2]
    no=b[1::2]
    st=[]
    q=['']*len(alpha)
    for i in range(len(alpha)):
        q[i]=alpha[i]*int(no[i])
        st+=q[i]
    print(''.join(st))
else:
    print('Error')