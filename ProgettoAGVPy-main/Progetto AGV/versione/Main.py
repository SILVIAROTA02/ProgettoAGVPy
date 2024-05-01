from Metric import *
from Mappa import *
from Node import *
from Point import *
from ILawMotion import *
from Obstacle import *
from PathFinderSolver import *
from PointReachable import *

pericolosityDict={(0,4):1, (0,5):3, (4,4):2}   
mappa= Mappa(10, 10, [
                      Obstacle(ConstantVelocity(Point(2,3), Point(1,1))),
                      Obstacle(ConstantVelocity(Point(3,6), Point(1,2))),
                      Obstacle(ConstantVelocity(Point(3,2), Point(1,3))),
                      Obstacle(ConstantVelocity(Point(0,0), Point(0,2))),
                      Obstacle(ConstantVelocity(Point(1,0), Point(-1,1)))
], pericolosityDict)
start= PointReachable (3,3,0)
target= PointReachable (6,6,0)
heuristica= DistanzaManhattan()
solver= PathfinderSolver(mappa, heuristica, start, target)

lista = solver.solve()
print("path: ({})".format(len(lista)))
for i in lista: 
    print (i)
print ()
o = Obstacle(MotionPath(lista))
mappa.obstacle.append(o)
start1= PointReachable (4,2,0)
target1= PointReachable (4,5,0)
solver1= PathfinderSolver(mappa, heuristica, start1, target1)
lista1= solver1.solve()
print("path1: ({})".format(len(lista1)))
for i in lista1: 
    print (i)
