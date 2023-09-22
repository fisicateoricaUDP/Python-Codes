#!/bin/python3.9

# Animation of a binary star with Vpython.

from vpython import *

scene.caption = """1) To rotate camera drag with right button.
2) To zoom drag with middle button or use scroll wheel.
3) On a two-button mouse, middle is left + right.
4) Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""
scene.forward = vector(0,-.3,-1)

G = 6.7e-11 # Newton gravitational constant

giant = sphere(pos=vector(-1e11,0,0), radius=2e10, color=color.cyan, 
                make_trail=True, trail_type='points', interval=10, retain=50)
giant.mass = 2e30
giant.p = vector(0, 0, -1e4) * giant.mass

dwarf = sphere(pos=vector(1.5e11,0,0), radius=1e10, color=color.blue,
                make_trail=True, interval=10, retain=10)
dwarf.mass = 1e30
dwarf.p = -giant.p

dt = 1e5
while True:
    rate(200)
    r = dwarf.pos - giant.pos
    F = G * giant.mass * dwarf.mass * r.hat / mag(r)**2
    giant.p = giant.p + F*dt
    dwarf.p = dwarf.p - F*dt
    giant.pos = giant.pos + (giant.p/giant.mass) * dt
    dwarf.pos = dwarf.pos + (dwarf.p/dwarf.mass) * dt
