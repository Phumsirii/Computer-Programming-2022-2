# x=[0]*100+[1]*100+[2]*100
# print(x)


a=list(input())
b=list(input())
y=len(a)
z=len(b)
m=abs(y-z)
c=['']*(y+z+m)
c[::2]=a+['?']*(len(c[::2])-y)
c[1::2]=b+['?']*(len(c[1::2])-z)
print(c)