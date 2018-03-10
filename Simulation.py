import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

from Pendulum import *


PlotSize=1

G = 9.81  # acceleration due to gravity, in m/s^2
L = 1.0  # length of pendulum in m
DeltaT = 0.01 # time difference between pictures in s

Phi1deg=179.99
Phi2deg=179.999
Omega1deg=0
Omega2deg=0

#setup figure
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False,
                     xlim=(-PlotSize, PlotSize), ylim=(-PlotSize, PlotSize))
ax.set_aspect('equal')
ax.grid(True)

#setup pendulum
pendulum1 = Pendulum(ax, G, L, math.radians(Phi1deg), math.radians(Omega1deg))
pendulum2 = Pendulum(ax, G, L, math.radians(Phi2deg), math.radians(Omega2deg))

def initAnimation():
    todraw = pendulum1.init()
    todraw = pendulum2.init()
    return todraw


def updateAnimation(i):
    pendulum1.simulate(DeltaT)
    todraw = pendulum1.drawing()
    pendulum2.simulate(DeltaT)
    todraw += pendulum2.drawing()
    return todraw

ani = animation.FuncAnimation(fig, updateAnimation, None, interval=DeltaT*1000,
                              blit=True, init_func=initAnimation)

plt.show()
