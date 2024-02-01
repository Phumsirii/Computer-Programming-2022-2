class roman:
    def __init__(self,r):
        self.r=r
        self.i=0
        a=r.find('IV')
        if not a==-1:
            r=r[:a:]+r[a+2::]
            self.i+=4
        a=r.find('IX')
        if not a==-1:
            r=r[:a:]+r[a+2::]
            self.i+=9
        a=r.find('XL')
        if not a==-1:
            r=r[:a:]+r[a+2::]
            self.i+=40
        a=r.find('XC')
        if not a==-1:
            r=r[:a:]+r[a+2::]
            self.i+=90
        a=r.find('CD')
        if not a==-1:
            r=r[:a:]+r[a+2::]
            self.i+=400
        a=r.find('CM')
        if not a==-1:
            r=r[:a:]+r[a+2::]
            self.i+=900
        a=r.count('I')
        b=r.count('V')
        c=r.count('X')
        d=r.count('L')
        e=r.count('C')
        f=r.count('D')
        g=r.count('M')
        self.i+=a+b*5+c*10+d*50+e*100+f*500+g*1000
        
    def __lt__(self,rhs):
        return self.i<rhs.i
    
    def __str__(self):
        return self.r
    
    def __int__(self):
        return self.i
    
    def __add__(self,rhs):
        a=int(self)
        b=int(rhs)
        c=a+b
        d=''
        e=c//1000
        c-=1000*e
        d+='M'*e
        e=c//100
        c-=100*e
        if e==9:
            d+='CM'
        elif e>=5:
            d+='D'+'C'*(e%5)
        elif e==4:
            d+='CD'
        else:
            d+='C'*e
        e=c//10
        c-=e*10
        if e==9:
            d+='XC'
        elif e>=5:
            d+='L'+'X'*(e%5)
        elif e==4:
            d+='XL'
        else:
            d+='X'*e
        e=c
        if e==9:
            d+='IX'
        elif e>=5:
            d+='V'+'I'*(e%5)
        elif e==4:
            d+='IV'
        else:
            d+='I'*e
        return roman(d)
    
t, r1, r2 = input().split() 
a = roman(r1); b = roman(r2) 
if t == '1' : print(a < b) 
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b)) 
else : print(str(a + b))
