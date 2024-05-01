from Point import *
from ILawMotion import *

class Obstacle (Point, ILawMotion):
    
    def __init__(self, ilawMotion):
        self.iLawMotion= ilawMotion
    
    def evaluate(self, t):
        return self.iLawMotion.evaluate(t)

class MotionPath(ILawMotion):
    def __init__(self, lista):
        self.lista=lista
    def evaluate (self, t):
        return self.lista[t]

