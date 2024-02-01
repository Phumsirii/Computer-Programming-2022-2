a,b,c,d=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
if a>b :
    a,b=b,a
    if d>=a:
        if c>d:
            c-=a
        else:
            b=a+c+d
    else:
        c+=a
        b=a+c+d
else:
    if c>a and a>=b:
        d+=a
    if d>c :
        b+=2
    else:
        b*=2
print(a,b,c,d)