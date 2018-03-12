import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

from AnimatedObject import *
from Pendulum import *
from DoublePendulum import *


PlotSize=2

G = 9.81  # acceleration due to gravity, in m/s^2
L = 1.0  # length of pendulum in m
FrameTime = 0.01 # time difference between pictures in s
SimTimeStep = 0.001

Phi1deg=170
Phi2deg=170
Omega1deg=0
Omega2deg=0

#setup figure
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False,
                     xlim=(-PlotSize, PlotSize), ylim=(-PlotSize, PlotSize))
ax.set_aspect('equal')
ax.grid(True)

#setup pendulum
pendulum1 = DoublePendulum(ax, G, L, L, math.radians(Phi2deg), math.radians(Omega2deg), math.radians(Phi2deg), math.radians(Omega2deg), 0, 0, 1, 1)
pendulum2 = DoublePendulum(ax, G, L, L, math.radians(Phi2deg), math.radians(Omega2deg), math.radians(Phi2deg), math.radians(Omega2deg), 0, 0, 1, 1)

def initAnimation():
    todraw = pendulum1.init()
    todraw = pendulum2.init()
    return todraw


def updateAnimation(i):
    pendulum1.simulate('euler', FrameTime, SimTimeStep)
    todraw = pendulum1.drawing()
    pendulum2.simulate('runge–kutta', FrameTime, SimTimeStep)
    todraw += pendulum2.drawing()
    return todraw

ani = animation.FuncAnimation(fig, updateAnimation, None, interval=FrameTime*1000,
                              blit=True, init_func=initAnimation)

plt.show()
