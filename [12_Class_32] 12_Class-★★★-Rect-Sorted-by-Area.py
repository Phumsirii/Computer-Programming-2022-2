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
    def __str__(self):
        return str(self.lowerleft)+"-"+str(self.upperright) 

    def __lt__(self,r):
        p1=self.lowerleft
        p2=self.upperright
        p3=r.lowerleft
        p4=r.upperright
        return (p2.x-p1.x)*(p2.y-p1.y)<(p4.x-p3.x)*(p4.y-p3.y)
        
n = int(input()) 
rects = [] 
for i in range(n): 
 x1,y1,x2,y2 = [int(e) for e in input().split()]
 rects.append(Rect(Point(x1,y1), Point(x2,y2))) 
rects.sort()
for i in range(n): 
 print(rects[i])