from numpy import sin, cos

from AnimatedObject import *

class Pendulum(AnimatedObject):
    """Simulation of a pendulum"""
    def __init__(self,ax,g,l,phi,omega):
        self.ax = ax
        self.g = g
        self.l = l
        self.phi = phi
        self.omega = omega
        # create an empty line for later
        self.line, = ax.plot([], [], 'o-', lw=2)
        
    def init(self):
        self.line.set_data([],[])
        return self.line,
    
    def simulate(self, deltaT):
        self.omega -= self.g / self.l * sin(self.phi) * deltaT
        self.phi += self.omega * deltaT
        
    def drawing(self):
        xCoords=[0, sin(self.phi)]
        yCoords=[0, -cos(self.phi)]
        self.line.set_data(xCoords,yCoords)
        return self.line,
