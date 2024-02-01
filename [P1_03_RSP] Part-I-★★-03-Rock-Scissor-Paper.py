m=int(input())
r=0
p1=0
p2=0
for r in range(3*m):
    a,b=[str(e) for e in input().split()]
    if (a=='R' and b=='S') or (a=='S' and b=='P') or (a=='P' and b=='R'):
        p1+=1
    if (b=='R' and a=='S') or (b=='S' and a=='P') or (b=='P' and a=='R'):
        p2+=1
    if p1==m or p2==m: break
if p1==m:
    print(p1,p2)
    print('Player 1 wins')
if m==p2:
    print(p1,p2)
    print('Player 2 wins')
if m>p1 and m>p2:
    print(p1,p2)
    print('Tie')