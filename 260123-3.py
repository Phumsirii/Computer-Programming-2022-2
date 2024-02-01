x=list(input())
y=list(input())
z=['']*max(len(x),len(y))*2
if len(x)>len(y):
    z[::2]=x
    z[1::2]=y+['?']*int(len(x)-len(y))
if len(x)<len(y):
    z[::2]=x+['?']*int(len(y)-len(x))
    z[1::2]=y
if len(x)==len(y):
    z[::2]=x
    z[1::2]=y
print(z)