from numpy import sin, cos
import numpy as np

from AnimatedObject import *

class Pendulum(ODEsim):
    """Simulation of a pendulum"""
    def __init__(self, ax, g, l, phi, omega, x0, y0):
        self.ax = ax
        self.g = g
        self.l = l
        self.state = np.array([phi, omega])
        self.x0 = x0
        self.y0 = y0
        # create an empty line for later
        self.line, = ax.plot([], [], 'o-', lw=2)
    
    def init(self):
        self.line.set_data([],[])
        return self.line,
    
    def F(self, state):
        dOmega = - self.g / self.l * sin(state[0])
        dPhi = state[1]
        dState = np.array([dPhi, dOmega])
        return dState
    
    def calculateCoordinates(self):
        self.xCoords=[self.x0, self.x0 + self.l* sin(self.state[0])]
        self.yCoords=[self.y0, self.y0 - self.l* cos(self.state[0])]
    
    def drawing(self):
        self.calculateCoordinates()
        self.line.set_data(self.xCoords,self.yCoords)
        return self.line,
