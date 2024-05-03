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
start01= PointReachable (3,3,0)
target01= PointReachable (6,6,0)
heuristica= DistanzaManhattan()
AGV01= PathfinderSolver(mappa, heuristica, start01, target01)

lista = AGV01.solve()
print("Path AGV01: ({})".format(len(lista)))
for i in lista01: 
    print (i)
print ()
o = Obstacle(MotionPath(lista01))
mappa.obstacle.append(o)
start02= PointReachable (4,2,0)
target02= PointReachable (4,5,0)
AGV02= PathfinderSolver(mappa, heuristica, start02, target02)
lista1= AGV02.solve()
print("Path AGV02: ({})".format(len(lista02)))
for i in lista02: 
    print (i)
