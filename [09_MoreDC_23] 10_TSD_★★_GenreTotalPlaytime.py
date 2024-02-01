n=int(input())
b=[]
c=[]
for i in range(n):
    a=input().split(',')
    if a[-2].strip() in b:
        d=b.index(a[-2].strip())
        v=a[-1].strip().split(':')
        c[d][0]+=(int(v[1])+60*int(v[0]))
    else:
        b.append(a[-2].strip())
        v=a[-1].strip().split(':')
        c.append([(int(v[1])+60*int(v[0])),a[-2].strip()])
c.sort()
for i in c[-1:-4:-1]:
    print(i[1],'-->',str(i[0]//60)+':'+'0'*(2-len(str(i[0]%60)))+str(i[0]%60))