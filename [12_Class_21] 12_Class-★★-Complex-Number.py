def pr(r,i):
    if r==0:
        if i==0:
            return '0'
        elif i==1:
            return 'i'
        elif i==-1:
            return '-i'
        else:
            return str(i)+'i'
    else:
        if i==0:
            return str(r)
        elif i==1:
            return str(r)+'+i'
        elif i==-1:
            return str(r)+'-i'
        elif i>0:
            return str(r)+'+'+str(i)+'i'
        else:
            return str(r)+str(i)+'i'
    
class Complex :
    def __init__(self,a,b):
        self.r=a
        self.im=b
    def __str__(self):
        r=self.r
        i=self.im
        return pr(r,i)
    def __add__(self, rhs):
        return pr(a+c,b+d)
    def __mul__(self, rhs):
        return pr(a*c-b*d,a*d+b*c)
    def __truediv__(self, rhs):
        return pr(round((a*c+b*d)/(c**2+d**2),1),round((-a*d+b*c)/(c**2+d**2),1))

t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 :print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2) 
else : print(c1/c2)
