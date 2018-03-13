import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

from AnimatedObject import *
from Pendulum import *
from DoublePendulum import *




G = 9.81
L1 = 0.7
L2 = 1
M1 = 2
M2 = 1
FrameTime = 0.01 # time difference between pictures in s
SimTimeStep = 0.001

Phi1deg=90
Phi2deg=180
Omega1deg=0
Omega2deg=0


PlotSize  = (L1 + L2) * 1.1
#setup figure
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False,
                     xlim=(-PlotSize, PlotSize), ylim=(-PlotSize, PlotSize))
ax.set_aspect('equal')
ax.grid(True)

#setup pendulum
pendulum1 = DoublePendulum(ax, G, L1, L2, math.radians(Phi1deg), math.radians(Omega2deg), math.radians(Phi2deg), math.radians(Omega2deg), 0, 0, M1, M2)
pendulum2 = DoublePendulum(ax, G, L1, L2, math.radians(Phi1deg), math.radians(Omega2deg), math.radians(Phi2deg), math.radians(Omega2deg), 0, 0, M1, M2)

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
