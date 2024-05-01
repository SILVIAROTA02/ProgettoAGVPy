from Metric import *
from Mappa import *
from Node import *
from Point import *
from ILawMotion import *
from Obstacle import *

class PathfinderSolver:
    def __init__(self, mappa, heuristic, start, target):
        self.mappa = mappa
        self.heuristic = heuristic #sottoclasse di metric che quindi tratto come Metrica. 
        self.startNode = Node(start)
        self.startNode.g = 0
        self.startNode.h = heuristic.distanceBetween(start, target)
        self.endNode = Node(target)
        self.openSet = [self.startNode]
        self.closedSet = []
    
    def solve(self):
        dict={(self.startNode.point.x, self.startNode.point.y, 0):self.startNode}
        
        while len(self.openSet) > 0: # ho ancora nodi da esplorare
            x = self._getMin() #nodo che dobbiamo esplorare migliore tra i disponibili
            self.openSet.remove(x) #lo rimuovo dalla lista di punti da esplorare
            self.closedSet.append(x) #lo inserisco nella lista di quelli già esplorati
            
            if (x.point.x, x.point.y) == (self.endNode.point.x, self.endNode.point.y):
                return x.getPath() #getpath lo invoco da Nodo
            # controllo se la posizione di x e uguale alla posizione target
            
            t = x.previousNodesCount #variabile locale che rappresenta il tempo unitario 
            # map mappa gli elementi della lista restituita da mappa.neighbourOf (dove restituisce i punti) diventando cosi una lista di nodi
            for y in map(lambda p: dict.get((p.x,p.y,t+1), Node(p, t+1)), self.mappa.neighbourOf(x.point, t+1)):
                dict[(y.point.x,y.point.y,t+1)]=y
                
                if y in self.closedSet : 
                    continue
                #codice per calcolare il tentativo g (x.g(percorso tra start e x)+ euristica)
                tentative_g = x.g + self.heuristic.distanceBetween(x.point, y.point) #metodo dalla metrica
                tentativeIsBetter = False #salvo in una variabile per capire se il tentativo è il migliore trovato fino a quel momento.
                
                # criterio per capire se il tentaivo è migliore
                if y not in self.openSet:
                    self.openSet.append(y)
                    tentativeIsBetter = True
                elif tentative_g < y.g:
                    tentativeIsBetter = True
                #logica da fare se il tentavo è migliore
                if tentativeIsBetter:
                    y.previousNode = x
                    y.previousNodesCount = x.previousNodesCount + 1
                    y.g = tentative_g
                    y.h = self.heuristic.distanceBetween(y.point, self.endNode.point)
                    y.f = y.g + y.h
        
        return []

    def _getMin(self):
        x = self.openSet[0]
        for i in range(1, len(self.openSet)):
            x = Node.getMin(x, self.openSet[i]) #itera i punti dell'open set e restituisce quello che ha valore di f (prima) e poi criterio di pericolosità minore
        return x
