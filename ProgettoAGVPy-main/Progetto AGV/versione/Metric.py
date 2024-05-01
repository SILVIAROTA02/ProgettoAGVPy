import math
class Metric:
    
    def distanceBetween(self, a, b):
        pass

class DistanzaManhattan(Metric):

    def distanceBetween(self, a, b): #formula 
        return (abs(a.x-b.x)+ abs (a.y-b.y))
    
class DistanzaEuclidea(Metric):

    def distanceBetween(self, a, b):
        return math.sqrt(pow((a.x-b.x),2)+ pow((a.y-b.y),2))
