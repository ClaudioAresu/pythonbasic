
class coord():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coord = (self.x, self.y)
    
    def move(self, x, y):
        self.x += x
        self.y += y

    def __add__(self, p):
        return coord(self.x + p.x, self.y + p.y)
    def __sub__(self, p):
        return coord(self.x - p.x, self.y - p.y)
    def __mul__(self, p):
        return coord(self.x * p.x, self.y * p.y)
    def __str__(self):
        return "(" + str(self.x)+'x' + str(self.y) + ')'


p1 = coord(3, 4 )
p2 = coord(2, 1)
p3 = p1 + p2

print(p3)                
    
