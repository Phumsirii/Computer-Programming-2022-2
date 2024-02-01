a=[0,'January','February','March','April','May','June','July','August','September','October','November','December']
b=str(input())
c=b.split('/')
print(a[int(c[1])],c[0]+',',c[2])