a=[0,'R','Y','G','W','B','P','K']
c=[0,'R','Y','G','W','B','P','K']
s=[0,0,0]
r=6
while r>0:
    b=input()
    for i in b[1::]:
        if i in a[2::]:
            s[int(b[0])]+=a.index(i)
        elif i=='R':
            r-=1
            s[int(b[0])]+=1
while len(a)>2:
    b=input()
    if b[1] in a[2::]:
        s[int(b[0])]+=c.index(b[1])
        a.remove(b[1])
print(str(s[1]),str(s[2]))
if s[1]>s[2]:
    print('Player 1 wins')
elif s[1]<s[2]:
    print('Player 2 wins')
else:
    print('Tie')