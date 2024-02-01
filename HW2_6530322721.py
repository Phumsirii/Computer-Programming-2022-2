import math
f=math.sin
def riemann_left(f, a, b, n):
    a=float(a)
    b=float(b)
    n=float(n)
    dx=(b-a)/n
    x=a
    area=0
    while x<b:
        area+=dx*f(x)
        x+=dx
    return area
def riemann_right(f, a, b, n):
    a,b,n=[float(i) for i in [a,b,n]]
    dx=(b-a)/n
    x=a+dx
    area=0
    while x<=b:
        area+=dx*f(x)
        x+=dx
    return area
def riemann_mid(f,a,b,n):
    a,b,n=[float(i) for i in [a,b,n]]
    dx=(b-a)/n
    x=a+dx/2
    area=0
    while x<=(b-dx/2):
        area+=dx*f(x)
        x+=dx
    return area
def riemann_trap(f,a,b,n):
    a,b,n=[float(i) for i in [a,b,n]]
    dx=(b-a)/n
    x=a
    area=0
    while x<b:
        area+=0.5*(f(x)+f(x+dx))*dx
        x+=dx
    return area
def estimate(riemann_sum_function, f, a, b, precision):
    k=1
    while round(riemann_sum_function(f, a, b, k),precision)!=round(riemann_sum_function(f, a, b, k+1),precision):
        k+=1
        riemann_sum=riemann_sum_function(f, a, b, k)
    return [round(riemann_sum, precision), k]

import math

def f(x):
    return x**2 - x**3

def test_riemann_left():
    print('test_riemann_left()')
    x = riemann_left(math.sin, math.pi/3, 2*math.pi/3, 20)
    print('1:', round(x, 5))
    x = riemann_left(math.sin, math.pi/3, 2*math.pi/3, 75)
    print('2:', round(x, 5))
    x = riemann_left(math.sin, math.pi/3, 2*math.pi/3, 150)
    print('3:', round(x, 5))
    x = riemann_left(math.cos, 0, math.pi/2, 20)
    print('4:', round(x, 5))
    x = riemann_left(math.cos, 0, math.pi/2, 75)
    print('5:', round(x, 5))
    x = riemann_left(math.cos, 0, math.pi/2, 150)
    print('6:', round(x, 5))
    x = riemann_left(f, 0, 1, 10)
    print('7:', round(x, 5))
    x = riemann_left(f, 0, 1, 100)
    print('8:', round(x, 5))
    x = riemann_left(f, 0.3, 0.7, 10)
    print('9:', round(x, 5))
    x = riemann_left(f, 0.3, 0.7, 100)
    print('10:', round(x, 5))

def test_riemann_right():
    print('test_riemann_right()')
    x = riemann_right(math.sin, math.pi/3, 2*math.pi/3, 20)
    print('1:', round(x, 5))
    x = riemann_right(math.sin, math.pi/3, 2*math.pi/3, 75)
    print('2:', round(x, 5))
    x = riemann_right(math.sin, math.pi/3, 2*math.pi/3, 150)
    print('3:', round(x, 5))
    x = riemann_right(math.cos, 0, math.pi/2, 20)
    print('4:', round(x, 5))
    x = riemann_right(math.cos, 0, math.pi/2, 75)
    print('5:', round(x, 5))
    x = riemann_right(math.cos, 0, math.pi/2, 150)
    print('6:', round(x, 5))
    x = riemann_right(f, 0, 1, 10)
    print('7:', round(x, 5))
    x = riemann_right(f, 0, 1, 100)
    print('8:', round(x, 5))
    x = riemann_right(f, 0.3, 0.7, 10)
    print('9:', round(x, 5))
    x = riemann_right(f, 0.3, 0.7, 100)
    print('10:', round(x, 5))

def test_riemann_mid():
    print('test_riemann_mid()')
    x = riemann_mid(math.sin, math.pi/3, 2*math.pi/3, 20)
    print('1:', round(x, 5))
    x = riemann_mid(math.sin, math.pi/3, 2*math.pi/3, 75)
    print('2:', round(x, 5))
    x = riemann_mid(math.sin, math.pi/3, 2*math.pi/3, 150)
    print('3:', round(x, 5))
    x = riemann_mid(math.cos, 0, math.pi/2, 20)
    print('4:', round(x, 5))
    x = riemann_mid(math.cos, 0, math.pi/2, 75)
    print('5:', round(x, 5))
    x = riemann_mid(math.cos, 0, math.pi/2, 150)
    print('6:', round(x, 5))
    x = riemann_mid(f, 0, 1, 10)
    print('7:', round(x, 5))
    x = riemann_mid(f, 0, 1, 100)
    print('8:', round(x, 5))
    x = riemann_mid(f, 0.3, 0.7, 10)
    print('9:', round(x, 5))
    x = riemann_mid(f, 0.3, 0.7, 100)
    print('10:', round(x, 5))

def test_riemann_trap():
    print('test_riemann_trap()')
    x = riemann_trap(math.sin, math.pi/3, 2*math.pi/3, 20)
    print('1:', round(x, 5))
    x = riemann_trap(math.sin, math.pi/3, 2*math.pi/3, 75)
    print('2:', round(x, 5))
    x = riemann_trap(math.sin, math.pi/3, 2*math.pi/3, 150)
    print('3:', round(x, 5))
    x = riemann_trap(math.cos, 0, math.pi/2, 20)
    print('4:', round(x, 5))
    x = riemann_trap(math.cos, 0, math.pi/2, 75)
    print('5:', round(x, 5))
    x = riemann_trap(math.cos, 0, math.pi/2, 150)
    print('6:', round(x, 5))
    x = riemann_trap(f, 0, 1, 10)
    print('7:', round(x, 5))
    x = riemann_trap(f, 0, 1, 100)
    print('8:', round(x, 5))
    x = riemann_trap(f, 0.3, 0.7, 10)
    print('9:', round(x, 5))
    x = riemann_trap(f, 0.3, 0.7, 100)
    print('10:', round(x, 5))

def test_estimate():
    print('test_estimate()')
    k = estimate(riemann_left, math.sin, math.pi/3, 2*math.pi/3, 5)
    print('1:', k)
    k = estimate(riemann_left, math.cos, 0, math.pi/2, 5)
    print('2:', k)
    k = estimate(riemann_left, f, 0.3, 0.7, 5)
    print('3:', k)
    k = estimate(riemann_right, math.sin, math.pi/3, 2*math.pi/3, 5)
    print('4:', k)
    k = estimate(riemann_right, math.cos, 0, math.pi/2, 5)
    print('5:', k)
    k = estimate(riemann_right, f, 0.3, 0.7, 5)
    print('6:', k)
    k = estimate(riemann_mid, math.sin, math.pi/3, 2*math.pi/3, 5)
    print('7:', k)
    k = estimate(riemann_mid, math.cos, 0, math.pi/2, 5)
    print('8:', k)
    k = estimate(riemann_mid, f, 0.3, 0.7, 5)
    print('9:', k)
    k = estimate(riemann_trap, math.sin, math.pi/3, 2*math.pi/3, 5)
    print('10:', k)
    k = estimate(riemann_trap, math.cos, 0, math.pi/2, 5)
    print('11:', k)
    k = estimate(riemann_trap, f, 0.3, 0.7, 5)
    print('12:', k)


test_riemann_left()
print('-'*20)
test_riemann_right()
print('-'*20)
test_riemann_mid()
print('-'*20)
test_riemann_trap()
print('-'*20)
test_estimate()