def spiral_square(n):
    if n==1:
        return [[1]]
    else:
        a=[[5,4,3],[6,1,2],[7,8,9]]
        b=10
        for i in range(3,n,2):
            for e in range(-1,-len(a)-1,-1):
                a[e].append(b)
                b+=1
            c=[]
            for e in range(1,len(a)+3):
                c.insert(0,b)
                b+=1
            a.insert(0,c)
            for e in range(len(a)-1):
                a[e+1].insert(0,b)
                b+=1
            d=[]
            for e in range(len(a)+1):
                d.append(b)
                b+=1
            a.append(d)
        return a

def print_square(s):
    for i in range(len(s)):
        print(' '.join([(2*' '+str(e))[-3:] for e in s[i]]))

exec(input().strip())