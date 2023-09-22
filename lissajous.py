#!/bin/python3.9

from vpython import sphere, vector, rate, curve, color, canvas, scene
from math import sin, pi
from numpy import arange

scene = canvas(title = "Lissajous Figures")

scene.caption = """Some instructions:
1) To ratate camera dragh with right button.
2) To zoom drag with middle or use scroll wheel.
3) On a two-button mouse, middle is left+right. """
scene.forward = vector(0,0,-1)

w1 = float(input("Ingrese la frecuencia w1 [kHz]: "))
w2 = float(input("Ingrese la frecuencia w2 [kHz]: "))
deg = float(input("Ingrese el desfase [°]: "))
der = deg*pi/180

s = sphere(pos=vector(1,0,0), radius=0.1)
s.color = color.green
curva = curve(color = color.green)

for theta in arange(0,100*pi,0.01):
    rate(200)
    x = 2*sin(w1*theta)
    y = 4*sin(w2*theta + der)
    s.pos = vector(x,y,0)
    curva.append(pos=s.pos)    
