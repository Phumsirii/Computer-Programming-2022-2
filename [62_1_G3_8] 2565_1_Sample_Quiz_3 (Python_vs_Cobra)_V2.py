n=int(input())
party=[]
parre={} #partyandresult
for i in range(n):
    a=input()
    party.append(a)
    parre[a]=[[0,'Y'],[0,'N'],[0,'X']] #YNX
n=int(input())
mempar={} #membertoparty
for i in range(n):
    a=[i.strip() for i in input().split()]
    mempar[a[0]]=a[1]
n=int(input())
memde={} #membertovote
z={'Y':0,'N':1,'X':2}
for i in range(n):
    a=input().split()
    memde[a[0]]=a[1]
    parre[mempar[a[0]]][z[a[1]]][0]+=1
for i in parre:
    parre[i]=sorted(parre[i])
    if parre[i][2][0]==parre[i][1][0]:
        parre[i]='Inconclusive'
    else:
        parre[i]=parre[i][2][1]
cobra={}
for i in memde:
    a=mempar[i]
    if not a in cobra:
        cobra[a]=[]
    if memde[i]==parre[a]:
        pass
    elif parre[a]=='Inconclusive':
        cobra[a]=['Inconclusive']
    else:
        cobra[a].append(i)
        cobra[a].sort()
for i in party:
    if not i in cobra:
        cobra[i]=['Inconclusive']
    print(i)
    if cobra[i]==[]:
        print('No cobra')
    else:
        print(', '.join(cobra[i]))