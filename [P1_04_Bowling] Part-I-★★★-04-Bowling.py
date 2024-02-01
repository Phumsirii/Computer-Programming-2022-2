a=input()
b=[]
for n in range(len(a)):
    b.append(a[n])
c=[0]
while len(c)<=9:
    if b[0]=='X':
        b.remove('X')
        x=10
        if b[1]=='/':
            x+=10
        elif b[0]=='X':
            x+=10
            if b[1]=='X':
                x+=10
            else:
                x+=int(b[1])
        else:
            x+=(int(b[0])+int(b[1]))
        c.append(x)
    elif b[1]=='/':
        x=b.pop(0)
        y=b.pop(0)
        if b[0]=='X':
            c.append(20)
        else:
            c.append(10+int(b[0]))
    else:
        x=b.pop(0)
        y=b.pop(0)
        c.append(int(x)+int(y))
x=0
if len(b)==3:
    if b[0]=='X':
        x+=10
        if b[1]=='X':
            x+=10
            if b[2]=='X':
                x+=10
            else:
                x+=int(b[2])
        else:
            if b[2]=='X':
                x+=10
            elif b[2]=='/':
                x+=(10-int(b[1]))
            else:
                x+=int(b[2])
            x+=int(b[1])
    elif b[2]=='X':
        x+=20
    else:
        x+=(10+int(b[2]))
else:
    x+=(int(b[0])+int(b[1]))
c.append(x)
w=int(input())
if w in range(1,11):
    print(c[w])
else:
    print(sum(c))