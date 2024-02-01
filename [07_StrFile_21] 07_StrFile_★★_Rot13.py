a=['A','B','C','D','E','F','G','H','I','J','K','L','M']
b=['N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
c=['a','b','c','d','e','f','g','h','i','j','k','l','m']
d=['n','o','p','q','r','s','t','u','v','w','x','y','z']
e=input()
f=[]
def rot(x):
    g=''
    for i in range(len(x)):
        if x[i] in a:
            g+=b[a.index(x[i])-13]
        elif x[i] in b:
            g+=a[b.index(x[i])-13]
        elif x[i] in c:
            g+=d[c.index(x[i])-13]
        elif x[i] in d:
            g+=c[d.index(x[i])-13]
        else:
            g+=x[i]
    return g
while e!='end':
    f.append(rot(e))
    e=input()
for i in f:
    print(i)