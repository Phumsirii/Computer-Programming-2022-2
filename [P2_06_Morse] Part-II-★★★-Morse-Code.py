l=input()
a=open(l,'r')
b=a.readlines()
for i in range(len(b)-1):
    b[i]=b[i][:-1:]
t=b[1]
u=[]
v=[]
j=0
while j<len(t)-1:
    c=t.find('[',j)
    u.append(t[c+1])
    d=t.find('[',j+1)
    v.append(t[c+3:d])
    j=d
if b[0]=='T2M':
    for i in b[2::]:
        z=False
        y=''
        for e in i:
            if not e in u:
                z=True
                break
            else:
                y+=v[u.index(e)]+' '
        if z:
            print('Invalid :',i)
        else:
            print(y.strip())
elif b[0]=='M2T':
    for i in b[2::]:
        z=False
        y=''
        for e in i.split():
            if not e in v:
                z=True
                break
            else:
                y+=u[v.index(e)]
        if z:
            print('Invalid :',i)
        else:
            print(y.strip())
else:
    print('Invalid code')