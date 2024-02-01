n=int(input())
a=[]
for i in range(n):
    b=input()
    if b=='':
        a.append('')
    else:
        e=0
        while b[e]=='.':
            e+=1
        a.append(b[int(e/2)::])
for i in a:
    print(i)