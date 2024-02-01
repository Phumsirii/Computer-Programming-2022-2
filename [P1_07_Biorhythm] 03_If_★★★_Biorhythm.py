def day_of_year(d, m, y):
    d=int(d)
    m=int(m)
    y=int(y)-543
    m1=[31,28,31,30,31,30,31,31,30,31,30,31]
    m2=[31,29,31,30,31,30,31,31,30,31,30,31]
    if y%4==0 and y%100!=0:
        months=m2[:m-1:]
        sm=int(sum(months))
        days=sm+d
    else:
        if y%400==0:
            months=m2[:m-1:]
            sm=int(sum(months))
            days=sm+d
        else:
            months=m1[:m-1:]
            sm=int(sum(months))
            days=sm+d
    return days
z=input()
y=z.split()
bd=int(y[0])
bm=int(y[1])
by=int(y[2])
d=int(y[3])
m=int(y[4])
y=int(y[5])
import math
a=day_of_year(bd, bm, by)
b=day_of_year(d, m, y)
c=(int(y)-int(by)-1)*365
if (by-543)%4==0 and (by-543)%100!=0:
    d=366-a
else:
    if (by-543)%400==0:
        d=366-a
    else:
        d=365-a
t=d+c+b
p="{:.2f}".format(math.sin(2*(math.pi)*t/23))
e="{:.2f}".format(math.sin(2*(math.pi)*t/28))
i="{:.2f}".format(math.sin(2*(math.pi)*t/33))
print(t,p,e,i)