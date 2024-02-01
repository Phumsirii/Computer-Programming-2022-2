def get_product_from_file(textfile):
    t=open(textfile,'r')
    a=t.readlines()
    b={}
    for i in a:
        c=i.split('=')
        b[c[0].strip()]=c[1].strip()
    b['created_date']=b['created_date'][:2]+'/'+b['created_date'][2:4]+'/'+b['created_date'][4::]
    t.close()
    return b
#print(get_product_from_file('002.txt'))
#print(get_product_from_file('008.txt'))
#print(get_product_from_file('007.txt'))

def cal_defect_ratio(textfile):
    t=open(textfile,'r')
    a=t.readlines()
    for i in range(len(a)):
        a[i]=a[i].strip()
    a.sort()
    b=a[-1]
    c=b.split('=')
    p=0
    n=0
    for i in c[1].strip():
        if i=='+':
            p+=1
        elif i=='-':
            n+=1
    t.close()
    return round(p/(n+p),2)
#print(cal_defect_ratio('008.txt'))
#print(cal_defect_ratio('007.txt'))

def cal_defect_box_ratio(textfile):
    t=open(textfile,'r')
    a=t.readlines()
    for i in range(len(a)):
        a[i]=a[i].strip()
    a.sort()
    b=a[-1].split('=')
    c=['']+b[-1].strip().split(',')
    d=len(c)-1
    e=int(round(d**(1/3),1))
    f=int(e**2)
    h=[]
    w=[]
    l=[]
    for i in range(1,len(c)):
        if c[i]=='+':
            h.append(((i-1)//f)+1)
            w.append((i-1)%e+1)
            l.append(((i-1)%f//e)+1)
    if len(h)==0:
        return float(0)
    h=max(h)-min(h)+1
    w=max(w)-min(w)+1
    l=max(l)-min(l)+1
    t.close()
    return round(h*w*l/d,2)
#print(cal_defect_box_ratio("008.txt"))
#print(cal_defect_box_ratio("007.txt"))

def create_prod_summary_file(pids):
    if pids==[]:
        return None
    pids.sort()
    a=open('product_summary.csv','w')
    for i in range(len(pids)-1):
        b=pids[i]
        c=get_product_from_file(b+'.txt')
        d=cal_defect_ratio(b+'.txt')
        e=cal_defect_box_ratio(b+'.txt')
        a.write(b+','+c['created_date']+','+c['factory_id']+','+str(d)+','+str(e)+'\n')
    b=pids[-1]
    c=get_product_from_file(b+'.txt')
    d=cal_defect_ratio(b+'.txt')
    e=cal_defect_box_ratio(b+'.txt')
    a.write(b+','+c['created_date']+','+c['factory_id']+','+str(d)+','+str(e))
    a.close()
create_prod_summary_file(["001","199","003","004","ABCD","002","010","009","008","007","005"])

def create_size_summary_file(pids):
    if pids==[]:
        return None
    a={}
    for i in pids:
        a[i]=cal_defect_box_ratio(i+'.txt')
    s=0
    m=0
    l=0
    for i in a:
        if a[i]<0.33:
            s+=1
        elif 0.33<=a[i]<0.67:
            m+=1
        elif a[i]>=0.67:
            l+=1
    b=open('size_summary.csv','w')
    b.write('size,#\n')
    b.write('S'+','+str(s)+'\n')
    b.write('M'+','+str(m)+'\n')
    b.write('L'+','+str(l))
    b.close()
#create_size_summary_file(["001","199","003","004","002","010","009","008","007","005"])