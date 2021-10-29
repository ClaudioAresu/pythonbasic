from collections import namedtuple

Points = namedtuple('Points', 'x y z')

newPoints = Points(3, 4 , 5)
print(newPoints.x, newPoints.y, newPoints.z)
print(newPoints[0])
print(newPoints._asdict())
print(newPoints._fields)

print(newPoints._replace(y=7))
p2 = Points._make(['a', 'b', 'c'])
print(p2)