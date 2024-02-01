a=[0,'A','2','3','4','5','6','7','8','9','T','J','Q','K']
b=[0,'C','D','H','S']
z=input()
c=[]
for i in z:
    c.append(i)
d=[]
for i in range(0,len(c)-3,2):
    if c[i]==c[i+2]:
        d.append(b.index(c[i+1])-b.index(c[i+3]))
    else:
        d.append(a.index(c[i])-a.index(c[i+2]))
e=[]
for i in d:
    if i>0:
        e.append('+'+str(i))
    else:
        e.append(str(i))
print(''.join(e))