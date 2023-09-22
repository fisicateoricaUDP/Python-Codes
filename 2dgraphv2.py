#!/bin/python3.9                                                                                          
from vpython import *

tgraph = graph(title = "Gráfica de Prueba", xtitle = "x [m]", ytitle = "f(x) [m^3]")
f1 = gcurve(color = color.blue)

x = -3
dx = 0.01
a = -3
da = 0.01

while a < 3:
    rate(50)
    data = []
    x = -3
    while x < 3:
        fx = a*x**3 - 3
        data = data + [(x, fx)]
        x = x + dx

    f1.data = data
    a = a + da
