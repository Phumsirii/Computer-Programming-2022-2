def feb29(a):
    if (a-543)%400==0 or ((a-543)%4==0 and (a-543)%100!=0):
        return True
    else:
        return False

def date(f):
    a=[int(b) for b in f[-3::]]
    b=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    c=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    if feb29(a[-1]):
        if b[a[-2]]>=a[0]>0:
            return True
        else:
            return False
    else:
        if c[a[-2]]>=a[0]>0:
            return True
        else:
            return False

def nex(dmy,d):
    dmy=[int(b) for b in dmy[-3::]]
    if feb29(dmy[2]):
        a=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        a=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    if a[dmy[1]]-dmy[0]>=d:
        dmy[0]+=d
    else:
        if dmy[1]==12:
            d-=a[dmy[1]]-dmy[0]
            dmy[1]=1
            dmy[0]=d
            dmy[2]+=1
        else:
            d-=a[dmy[1]]-dmy[0]
            dmy[1]+=1
            dmy[0]=d
    return dmy

a=[]
b=input().split()
while b[0]!='END':
    a.append(b)
    b=input().split()
c=[]
e=[]
for i in a:
    if int(i[-1])<2558:
        c.append(['Error:',' '.join(i),'-->','Invalid year'])
    elif not 0<int(i[-2])<13:
        c.append(['Error:',' '.join(i),'-->','Invalid month'])
    elif not date(i):
        c.append(['Error:',' '.join(i),'-->','Invalid date'])
    elif not i[1] in 'EQNF':
        c.append(['Error:',' '.join(i),'-->','Invalid delivery type'])
    else:
        if i[1]=='E':
            d=1
        elif i[1]=='Q':
            d=3
        elif i[1]=='N':
            d=7
        elif i[1]=='F':
            d=14
        e.append([nex(i[-3::1],d)[-1::-1],i[0]])
for i in c:
    print(' '.join(i))
e.sort()
for i in e:
    a=[str(o) for o in i[0][-1::-1]]
    b=i[1]+':'
    print(b,'delivered on','/'.join(a))