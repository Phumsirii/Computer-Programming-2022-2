import csv
fn = open('athlete_events_2000-2016_cl.csv', 'r', encoding='utf-8-sig') 
data = list(csv.reader(fn, delimiter = ','))
fn.close()

fn = open('athlete_events_mock.csv', 'r', encoding='utf-8-sig') 
data_mock = list(csv.reader(fn, delimiter = ','))
fn.close()

def convert_to_dict(data):
    a={}
    for i in data[1::]:
        b={}
        for e in range(len(data[0])):
            b[data[0][e]]=i[e]
        if i[9] in a:
            if i[7] in a[i[9]]:
                a[i[9]][i[7]].append(b)
            else:
                a[i[9]][i[7]]=[b]
        else:
            a[i[9]]={}
            a[i[9]][i[7]]=[b]
    return a

def get_medals_by_team(athletes_by_Year_Noc,year):
    a=athletes_by_Year_Noc[year]
    b={}
    for i in a:
        b[i]=[0,0,0]
        for e in a[i]:
            if e['Medal']=='Gold':
                b[i][0]+=1
            elif e['Medal']=='Silver':
                b[i][1]+=1
            elif e['Medal']=='Bronze':
                b[i][2]+=1
        b[i]=tuple(b[i])
    return b

def get_top_five(medals):
    a=[[-a for a in medals[i]]+[i] for i in medals]
    a.sort()
    if len(a)<=5:
        return [tuple([e[3]]+[-a for a in e[:3:]]) for e in a]
    b=a[:5:]
    i=5
    while a[i][:3]==a[4][:3]:
        b.append(a[i])
        i+=1
    return [tuple([e[3]]+[-a for a in e[:3:]]) for e in b]

def get_medals_trend(athletes_by_year_NOC,NOC,start,end):
    a=[]
    for i in athletes_by_year_NOC:
        if start<=int(i)<=end:
            if NOC in get_medals_by_team(athletes_by_year_NOC,i):
                a.append((i,)+get_medals_by_team(athletes_by_year_NOC,i)[NOC])
            elif NOC in athletes_by_year_NOC[i] :
                a.append((i,0,0,0))
    return sorted(a)

def get_sports(athletes_by_Year_NOC,NOC,year):
    a=set()
    if year in athletes_by_Year_NOC and NOC in athletes_by_Year_NOC[year]:
        for i in athletes_by_Year_NOC[year][NOC]:
            if i['Medal']!='NA':
                a.add(i['Sport'])
    return a

def get_common_sports(athletes_by_Year_NOC, NOCs,year):
    if len(NOCs)==0:
        return set()
    a=tuple(NOCs)
    if not year in athletes_by_Year_NOC:
        return set()
    b=get_sports(athletes_by_Year_NOC,a[0],year)
    for i in a[1::]:
        c=get_sports(athletes_by_Year_NOC,i,year)
        b=b&c
        if b==set():
            return set()
    return b

d_mock = convert_to_dict(data_mock)
m_mock = get_medals_by_team(d_mock, '2010')
print(get_top_five(m_mock))