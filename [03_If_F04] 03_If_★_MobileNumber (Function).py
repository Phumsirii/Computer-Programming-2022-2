def is_mobile_number(number):
    b=number[0:2:1]
    c=int(len(number))
    d=b=='06' or b=='08' or b=='09'
    g=c==10
    return d and g
exec(input())