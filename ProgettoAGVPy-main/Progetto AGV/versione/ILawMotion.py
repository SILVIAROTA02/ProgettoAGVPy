from Point import *

class ILawMotion:
    
    def evaluate(self, t):
        pass

class ConstantVelocity (ILawMotion):

    def __init__(self,velocity, initialPosition):
        self.velocity= velocity
        self.initialPosition= initialPosition
    
    def evaluate(self, t):
        return self.velocity*t + self.initialPosition
