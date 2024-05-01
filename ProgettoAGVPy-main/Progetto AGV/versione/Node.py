from PointReachable import *

class Node():
    def __init__(self, point, t=0):
        self.point = point
        self.previousNode = None #valore nullo, lo assegno dopo nell'algoritmo
        self.previousNodesCount = t
        self.g = float("inf") # Il valore di g è generalmente molto elevato
        self.h = 0
        self.f = 0
   
    def getPath(self):
        return self.getPathHelper([])

    def getPathHelper(self, path):
        path.insert(0, self.point) #inserimento nella posizione iniziale
        if self.previousNode is not None:
            self.previousNode.getPathHelper(path)
        return path

    def getMin(a, b):
        return a if a.f < b.f else b if b.f < a.f else \
               a if a.previousNodesCount<b.previousNodesCount else\
               b if b.previousNodesCount<a.previousNodesCount else\
               a if PointReachable.getMin(a.point, b.point)==a.point else b
    
    def __eq__(self, other):
        return self.point==other.point and self.previousNodesCount==other.previousNodesCount
