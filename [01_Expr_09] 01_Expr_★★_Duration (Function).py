def str2hms(hms_str):
    t = hms_str.split(':')
    return int(t[0]),int(t[1]),int(t[2])
def hms2str(h,m,s):
    return ('0'+str(h))[-2:] + ':' + \
           ('0'+str(m))[-2:] + ':' + \
           ('0'+str(s))[-2:]
def to_sec(h,m,s):
    a=int(h)
    b=int(m)
    c=int(s)
    return a*3600+b*60+c
def to_hms(t):
    h=t//3600
    m=(t-h*3600)//60
    s=t-h*3600-m*60
    return h,m,s
def diff(h1,m1,s1,h2,m2,s2):
    t1=(int(h1))*3600+(int(m1))*60+(int(s1))
    t2=(int(h2))*3600+(int(m2))*60+(int(s2))
    dt=t2-t1
    dh=dt//3600
    dm=(dt-dh*3600)//60
    ds=dt-3600*dh-60*dm
    return dh,dm,ds
def main():
    hms_start = input()
    a=str2hms(hms_start)
    ti=int(a[0])*3600+int(a[1])*60+int(a[2])
    hms_end = input()
    b=str2hms(hms_end)
    tf=int(b[0])*3600+int(b[1])*60+int(b[2])
    dt=tf-ti
    c=to_hms(dt)
    d=hms2str(c[0],c[1],c[2])
    return print(d)
exec(input())