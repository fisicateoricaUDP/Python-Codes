#!/bin/python3.9

# Animation of some atomic nuclei. 

from vpython import *

canvas(background=color.white)

# Hydrogen Nucleus
sphere(pos=vector(-3e-15,5e-15,0),radius=1e-15,color=color.red)
text(text='Hydrogen Nucleus (1 proton)', pos=vector(1e-15,5e-15,0), height=0.5e-15,color=color.black)

# Deuterium Nucleus 
sphere(pos=vector(-3e-15,1e-15,0),radius=1e-15,color=color.white)
sphere(pos=vector(-2e-15,1e-15,1e-15),radius=1e-15,color=color.red)
text(text='Deuterium Nucleus (1 proton + 1 neutron)', pos=vector(1e-15,1e-15,0), height=0.5e-15,color=color.black)

# Helium-3 Nucleus
sphere(pos=vector(-3e-15,-3e-15,0),radius=1e-15,color=color.white)
sphere(pos=vector(-2e-15,-3e-15,1e-15),radius=1e-15,color=color.red)
sphere(pos=vector(-1.5e-15,-3e-15,0),radius=1e-15,color=color.red)
text(text='Helium-3 Nucleus (2 proton + 1 neutron)', pos=vector(1e-15,-3e-15,0), height=0.5e-15,color=color.black)
