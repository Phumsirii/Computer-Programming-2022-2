a=input().split()
b=open(a[0],'r')
c=[]
for i in b:
    d,e=i.strip().split()
    e=float(e)
    if d[:2:]==a[1][-2::]:
        c.append([e,d])
b.close()
c.sort()
s=0
for i in c:
    s+=i[0]
if len(c)==0:
    print('No data')
else:
    print(str(c[0][0]),str(c[-1][0]),str(s/len(c)))