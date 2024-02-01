d=int(input())
m=int(input())
y=int(input())-543
m1=[31,28,31,30,31,30,31,31,30,31,30,31]
m2=[31,29,31,30,31,30,31,31,30,31,30,31]
if y%4==0 and y%100 != 0:
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
print(days)