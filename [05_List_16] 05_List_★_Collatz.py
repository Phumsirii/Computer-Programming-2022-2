n=int(input())
a=[n]
while n!=1:
    if n%2==0:
        n//=2
        a.append(n)
    else:
        n=n*3+1
        a.append(n)
if len(a)>15:
    a=a[-15::1]
    b=[]
    for c in a:
        b.append(str(c))
    print('->'.join(b))
else:
    b=[]
    for c in a:
        b.append(str(c))
    print('->'.join(b))