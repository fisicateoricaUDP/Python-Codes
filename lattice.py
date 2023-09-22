#!/bin/python3.9

from vpython import sphere, vector, color, canvas

scene = canvas(title = "Red Cristalina", caption = "subtitulo cualquiera")
scene.center = vector(-0.8,-0.8,0) 
scene.forward = vector(-0.3,-1,-1)

L = int(input("Ingrese el numero de esferas en una fila: "))
R = float(input("Ingrese el radio de la esfera [nm]: "))

for i in range(-L//2,L//2,1):
    for j in range(-L//2,L//2,1):
        for k in range(-L//2,L//2,1):
            sphere(pos=vector(i,j,k),color=vector(0,0.78,0.69),radius=R)
