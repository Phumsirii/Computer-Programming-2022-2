q=[]
w=[] #newnext
w2=[] #nextorder
d=[]
t=0
p=0
n=int(input())
for i in range(n):
    a=input().split()
    d.append(a[0])
    if a[0]=='reset':
        q.append(int(a[1]))
    elif a[0]=='new':
        x=q.pop(0)
        w.append([x,int(a[1])])
        print('ticket',x)
        q.append(x+1)
    elif a[0]=='next' :
        x=w.pop(0)
        print('call',x[0])
        w2.append(x)
    elif a[0]=='order':
        x=w2.pop(-1)
        dt=int(a[1])-x[1]
        t+=dt
        p+=1
        print('qtime',x[0],dt)
    elif a[0]=='avg_qtime':
        avg=t/p
        print('avg_qtime', round(avg,4))