a=input().lower()
b={}
for i in a:
    if i in b:
        b[i]+=1
    elif 'a'<=i<='z':
        b[i]=1
c=[]
for i in b:
    c.append([-b[i],i])
c.sort()
for i in c:
    print(i[1],'->',str(-i[0]))