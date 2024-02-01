class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")" 

class Rect:
    def __init__(self, p1, p2):
        self.lowerleft = p1 
        self.upperright = p2 
    
    def area(self):
        p1=self.lowerleft
        p2=self.upperright
        return (p2.x-p1.x)*(p2.y-p1.y)
  
    def contains(self, p):
        p1=self.lowerleft
        p2=self.upperright
        return p1.x<=p.x<=p2.x and p1.y<=p.y<=p2.y
  
x1,y1,x2,y2 = [int(e) for e in input().split()] 
lowerleft = Point(x1,y1) 
upperright = Point(x2,y2) 
rect = Rect(lowerleft, upperright) 
print(rect.area()) 
m = int(input()) 
for i in range(m):
    x,y = [int(e) for e in input().split()]
    p = Point(x,y) 
    print(rect.contains(p))