n=int(input())
b={}
for i in range(n):
    a=input().split(',')
    if a[1].strip() not in b:
        b[a[1].strip()]=[a[0].strip()]
    else:
        b[a[1].strip()].append(a[0].strip())
    if a[2].strip() not in b:
        b[a[2].strip()]=[a[0].strip()]
    else:
        b[a[2].strip()].append(a[0].strip())
c=input().split(',')
for i in c:
    if i.strip() in b:
        print(i.strip(),'->',', '.join(b[i.strip()]))
    else:
        print(i.strip(),'->','Not found')