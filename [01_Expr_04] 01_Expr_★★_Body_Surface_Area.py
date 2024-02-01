import math
W=float(input())
H=float(input())
c=(W*H)**(0.5)/60
d=0.024265*(W**0.5378)*(H**0.3964)
b=math.log(10)
a=0.6157-0.0188*math.log(W)/b
e=0.0333*(W**a)*(H**0.3)
print(c)
print(d)
print(e)