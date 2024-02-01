a=input()
b=input()
c=input()
d=open(a,'r')
e=open(b,'r')
f=open(c,'r')
g=d.readlines()
h=e.readlines()
i=f.readlines()
j={}
for k in g:
    k=k.strip().split(',')
    j[k[0]]=k[1]
k={}
for l in h:
    l=l.strip().split(',')
    k[l[0]]=l[1]
for x in i:
    x=x.strip().split(',')
    if x[0] in j and x[1] in k:
        print(j[x[0]]+','+k[x[1]])
    else:
        print('record error')
d.close()
e.close()
f.close()