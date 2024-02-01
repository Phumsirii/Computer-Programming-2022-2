f=input().strip()
n=int(input())
r=''
for i in range(n//10):
    r+='-'*9+str(i+1)
if n%10!=0:
    r+='-'*(n%10)
print(r)
a=open(f,'r')
b='.'.join([i.strip() for i in a.readlines()]).split('.')
while len(b)>0:
    if len(b[0])>=n:
        c=b.pop(0)
    else:
        c=''
        while len(b)>0 and len((c+b[0]).strip('.'))<=n:
            d=b.pop(0)
            c+=d+'.'
    if c.strip('.')!='':
        print(c.strip('.'))
a.close()