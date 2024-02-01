a=input().split(',')
b={}
c=[]
while a[0]!='q':
    if not a[1].strip() in b:
        b[a[1].strip()]=[]
        c.append(a[1].strip())
    b[a[1].strip()].append(a[0].strip())
    a=input().split(',')
for i in c:
    print(i+':',', '.join(b[i]))