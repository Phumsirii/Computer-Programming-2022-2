a=int(input())
b=a/1000
c=int(round(a/10**4,1)*10)
d=a/10**6
e=int(round(a/10**7,1)*10)
f=a/10**9
g=int(round(a/10**10,1)*10)
if a<1000:
    print(a)
if 1000<a<10000:
    print(str(round(b,1))+'K')
if 10000<a<10**6:
    print(str(c)+'K')
if 10**6<a<10**7:
    print(str(round(d,1))+'M')
if 10**7<a<10**9:
    print(str(e)+'M')
if 10**9<a<10**10:
    print(str(round(f,1))+'B')
if 10**10<a:
    print(str(g)+'B')
if a==1000 or a==10000 or a==100000:
    print(str(int(a/1000))+'K')
if a==1000000 or a==10000000 or a==100000000 :
    print(str(int(a/1000000))+'M')
if a>=1000000000 and a%1000000000==0:
    print(str(int(a/1000000000))+'B')