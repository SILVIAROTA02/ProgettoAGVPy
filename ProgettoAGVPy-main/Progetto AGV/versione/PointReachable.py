from Point import *

class PointReachable(Point): 

    def __init__(self, x, y, pericolosity):
        super().__init__(x, y)
        self.pericolosity=pericolosity

    def __str__(self):
        return "x: {}, y: {}, pericolosity: {}".format(self.x,self.y, self.pericolosity)
    
    def getMin(a, b):
        return a if a.pericolosity < b.pericolosity else b
