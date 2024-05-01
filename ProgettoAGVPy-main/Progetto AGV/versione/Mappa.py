import Obstacle
from PointReachable import *

class Mappa:
    def __init__(self,w,h,obstacle,pericolosityDict):
        self.w=w
        self.h=h
        self.obstacle=obstacle
        self.pericolosityDict=pericolosityDict
    
    def neighbourOf(self,p, t) :
        lista = []
        self.addIfInside(p.add( 1, 0), t, lista)
        self.addIfInside(p.add( 0, 1), t, lista)
        self.addIfInside(p.add(-1, 0), t, lista)
        self.addIfInside(p.add( 0,-1), t, lista)
        self.addIfInside(p.add( 0, 0), t, lista)
        return lista
    
    def addIfInside(self,p, t, lista):
        if (self.isInside(p) and not self.isThereObstacleIn(p, t)):
            lista.append(PointReachable(p.x, p.y, self.pericolosityDict.get((p.x, p.y), 0))) #indice di defaul è zero
    
    def isInside(self, p) :
        return p.x>=0 and p.y>=0 and p.x< self.getWidth() and p.y< self.getHeight()
    
    def getWidth (self):
        return self.w
    
    def getHeight(self):
        return self.h
    
    def isThereObstacleIn(self, p, t): # O(obstacles.size())
        for o in self.obstacle :
            if (self.constrain(o.evaluate(t))==p) : 
                return True
        return False
    
    def constrain(self, p):
        return p.constrain(0, 0, self.getWidth()-1, self.getHeight()-1) # restituisce un punto che sta sulla mappa controllando che non sia fuori dai bordi. se i vincoli non sono rispettati restituisce un punto il più vicino possibile sulla mappa al bordo.

