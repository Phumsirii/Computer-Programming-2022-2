x = [int(e) for e in input().split()]
k=int(input())
y=[x[0],1]
for a in range(1,len(x)):
    if x[a]==x[a-1]:
        y[-1]+=1
    else:
        y.append(x[a])
        y.append(1)
w=y[1::2]
q=y[::2]
o=[]
for u in range(len(w)):
    if w[u]<k:
        o.append(q[u]*w[u])
print(sum(o))