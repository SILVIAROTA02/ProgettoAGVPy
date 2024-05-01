class Point:
    
    def __init__ (self, x, y):
        self.x=x
        self.y=y
    
    def constrain(self, minX, minY, maxX, maxY):
        return Point(max(minX, min(maxX, self.x)),
                     max(minY, min(maxY, self.y)));
    
    def add(self,dx,dy):
        return Point(self.x+dx,self.y+dy)
    
    def __eq__(self, other):
        return isinstance(other,Point) and self.x==other.x and self.y==other.y
    
    def __add__ (self, other):
        return Point (self.x+other.x, self.y+other.y)
    
    def __mul__ (self, v):
        return Point (self.x*v, self.y*v)
    
    def __str__(self):
        return "{} {}".format(self.x, self.y)
    
