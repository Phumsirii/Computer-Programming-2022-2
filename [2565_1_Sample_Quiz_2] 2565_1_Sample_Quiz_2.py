def eligible(a,b):
    if len(a)!=len(b):
        return False
    c=[]
    for i in a:
        c.append(i.lower())
    d=[]
    for i in b:
        d.append(i.lower())
    for i in c:
        if 'a'<=i<='z' and d[c.index(i)]!=i:
            return False
            break
    return True

def joi(i,v):
    g=''
    for a in i[:-1:]:
        g+=a+v
    g+=i[-1]
    return g

a=input()
b=input()
c=input()
d=open(a,'r')
e=d.readlines()

for i in range(len(e)):
    e[i]=e[i][:-1]
    
pathnames=[]
for i in e:
    m=[]
    n=0
    while '/' in i[n::]:
        f=i.find('/',n)
        m.append(i[n:f])
        n=f+1
    m.append(i[n::])
    pathnames.append(m)
for i in pathnames:
    for u in range(len(i)) :
        if eligible(b,i[u]) and len(i)>1 and not(len(i)==2 and ''in i):
            i[u]=c

l=[]
for i in pathnames:
    l.append(joi(i,'/'))
for i in l:
    print(i)
d.close()