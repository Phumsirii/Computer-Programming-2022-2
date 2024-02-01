x1,x2,x3,x4,x5=input().split()
if int(x1)-int(x5)>int(x2):
    if int(x2)>int(x3)+int(x1):
        if int(x3)+int(x5)>int(x4):
            print('C5')
        else:
            if int(x3)<int(x5):
                print('C6')
            else:
                print('C7')
            print('C8')
else:
    if int(x2)-int(x1)>int(x3):
        pass
    else:
        if int(x4)<int(x5)+int(x1):
            if int(x3)+int(x2)>int(x5):
                print('C3')
            else:
                print('C2')
            print('C4')
        else:
            print('C1')