class piggybank:
    
    def __init__(self):
        self.c1=0
        self.c2=0
        self.c5=0
        self.c10=0
        
    def add1(self,n):
        self.c1+=n
    
    def add2(self,n):
        self.c2+=n
        
    def add5(self,n):
        self.c5+=n
        
    def add10(self,n):
        self.c10+=n
    
    def __int__(self):
        return self.c1+(self.c2)*2+(self.c5)*5+(self.c10)*10
    
    def __lt__(self,r):
        return int(self)<int(r)
    
    def __str__(self):
        return '{1:'+str(self.c1)+', '+'2:'+str(self.c2)+', '+'5:'+str(self.c5)+', '+'10:'+str(self.c10)+'}'
        
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
