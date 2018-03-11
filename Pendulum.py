from numpy import sin, cos
import numpy as np

from AnimatedObject import *

class Pendulum(ODEsim):
    """Simulation of a pendulum"""
    def __init__(self,ax,g,l,phi,omega):
        self.ax = ax
        self.g = g
        self.l = l
        self.state = np.array([phi, omega])
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
    
    def drawing(self):
        xCoords=[0, sin(self.state[0])]
        yCoords=[0, -cos(self.state[0])]
        self.line.set_data(xCoords,yCoords)
        return self.line,
