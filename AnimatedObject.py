from abc import ABC, abstractmethod
import numpy as np

class AnimatedObject(ABC):
    
    @abstractmethod
    def __init__(self,ax):
        pass
    
    @abstractmethod
    def simulate(self, deltaT): # simulate forward a time of deltaT
        pass
    
    @abstractmethod
    def drawing(self): # return current picture
        pass

class ODEsim(AnimatedObject):
    
    @abstractmethod
    def F(self, state): # function which describes the connection between y(t)
        # and d/dt y(t): d/dt(y(t))=f(y(t))
        pass
    
    def iterateEuler(self,deltaT):
        dState = self.F(self.state)
        self.state += deltaT * dState
        
    def iterateRungeKutta(self,deltaT):
        k1 = self.F(self.state)
        k2 = self.F(self.state + deltaT * k1 / 2)
        k3 = self.F(self.state + deltaT * k2 / 2)
        k4 = self.F(self.state + deltaT * k3)
        self.state += deltaT / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    
    def simulate(self, ODEsolver, deltaT): # simulate forward by deltaT
        if ODEsolver.lower() == 'euler':
            self.iterateEuler(deltaT)
        elif ODEsolver.lower() == 'runge–kutta':
            self.iterateRungeKutta(deltaT)
        else:
            raise NotImplementedError("ODE solver not found")
        
