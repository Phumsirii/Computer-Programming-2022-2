a=[]
for n in range(9):
    a+=[input().split()]
b=[list(c) for c in a]
par=[]
stroke=[]
count=[]
d=[]
for n in range(9):
    par+=[b[n][0]]
    stroke+=[b[n][1]]
    count+=[b[n][2]]
    if count[n]=='1':
        d+=[min(int(par[n])+2,int(stroke[n]))]
    else:
        d+=[0]
sum_str=sum(int(e) for e in stroke)
sum_par=sum(int(e) for e in par)
sum_str2=sum(int(e) for e in d)
f=1.5*sum_str2-sum_par
g=float(f*0.8)
if g>=0:
    handi=int(g)
else:
    handi=int(g)-1
print(sum_str)
print(handi)
print(sum_str-handi)