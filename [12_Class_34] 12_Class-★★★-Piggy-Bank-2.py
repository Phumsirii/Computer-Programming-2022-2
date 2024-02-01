class piggybank:
    
    def __init__(self):
        self.coins={}
    
    def add(self,v,n):
        v=float(v)
        a=sum((self.coins).values())
        if a+n>100:
            return False
        if not v in self.coins:
            self.coins[v]=0
        self.coins[v]+=n
        return True
    
    def __float__(self):
        a=[(self.coins[i])*i for i in self.coins]
        return float(sum(a))
    
    def __str__(self):
        a=sorted([i for i in self.coins])
        b='{'
        c=[]
        for i in a:
            c.append(str(i)+':'+str(self.coins[i]))
        b+=', '.join(c)
        b+='}'
        return b

cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)