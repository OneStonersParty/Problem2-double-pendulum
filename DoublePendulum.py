from numpy import sin, cos
import numpy as np

from Pendulum import *

class DoublePendulum(Pendulum):
    """Simulation of a pendulum"""
    def __init__(self, ax, g, l, l2, phi, omega, phi2, omega2, x0, y0, m, m2):
        Pendulum.__init__(self, ax, g, l, phi, omega, x0, y0)
        self.state = np.concatenate((self.state, [phi2, omega2]))
        self.l2 = l2
        self.m = m
        self.m2 =m2
        self.alpha = 0
        self.alpha2 = 0
    
    def F(self, state):
        phi = state[0]
        omega = state[1]
        phi2 = state[2]
        omega2 = state[3]
        dOmega = - self.m2 / (self.m + self.m2) * self.l2 / self.l * \
                (self.alpha2 * cos(phi - phi2) + omega2 ** 2 * \
                sin(phi - phi2)) - self.g / self.l * sin(phi)
        dPhi = omega
        dOmega2 = - self.l / self.l2 * \
                (self.alpha * cos(phi - phi2) - omega ** 2 * \
                sin(phi - phi2)) - self.g / self.l2 * sin(phi2)
        dPhi2 = omega2
        self.alpha = dOmega
        self.alpha2 = dOmega2
        return np.array([dPhi, dOmega, dPhi2, dOmega2])
    
    def calculateCoordinates(self):
        Pendulum.calculateCoordinates(self)
        self.xCoords.append(self.xCoords[1] + self.l2 * sin(self.state[2]))
        self.yCoords.append(self.yCoords[1] - self.l2 * cos(self.state[2]))
