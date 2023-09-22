#!/usr/bin/env python3.9

from vpython import *
from numpy import sin
from math import factorial, pi

w1 = float(input("Ingrese la frecuencia w [kHz]: "))
A0 = float(input("Ingrese la amplitud A [m]: "))
o = int(input("Ingrese el orden de la serie de Taylor: "))

tgraph = graph(title = "Movimiento Armonico Simple",
               xtitle = "Angle [rad]",
               ytitle = "y = Asin(wt) [m]",
               foreground = color.black,
               background = color.yellow,
               xmin = -10, xmax = 10,
               ymin = -A0-1, ymax = A0+1)

f1 = gcurve(color=color.black, radius = 2)
f2 = gcurve(color=color.blue, radius = 2)
fp = gdots(color=color.red, radius = 2)

def func(z,n):
    s = 0
    for i in range(n+1):
        s += ((-1)**i/factorial(2*i+1))*(z**(2*i+1))
    return s

s = 0.01

x = -10
while x < 10:
    f1.plot(x, A0*sin(w1*x))
    x = x + s

#y = -10
#while y < 10:
#    rate(200)
#    data = [(y, A0*sin(w1*y))]
#    fp.data += data
#    y = y + s

n = 0
while n < o:
    rate(300)
    data = []
    z = -10
    while z < 10:
        fz = A0*func(w1*z,n)
        data = data + [(z, fz)]
        z = z + s

    f2.data += data

    y = -10
    fp.data = []
    while y < 10:
        rate(400)
        fp.data += [(y, A0*func(w1*y,n))]
        y = y + s
        
    n = n + 1

    


