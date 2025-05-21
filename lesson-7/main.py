class Vector2D:
    """Dunder methods"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other): # __eq__ is a dunder method for equality comparison
        print('executed')
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other): # __add__ is a dunder method for addition
        print("+ executed")
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector2D(new_x, new_y)
    

    def __sub__(self, other): # __sub__ is a dunder method for subtraction
        return Vector2D(self.x - other.x, self.y - other.y)

    def __str__(self): # __str__ is a dunder method for printing
        return f"Vector(x={self.x}, y={self.y})"


v1 = Vector2D(3, 5)
v2 = Vector2D(1, 3)
v3 = v1 + v2
v4 = v1 - v2

print(v3) # Vector(x=4, y=8)

if v1 == v2:
    print('Equal')
else:
    print("Inequal")
    
"""
Dunder methods
__init__
__str__
__repr__
__eq__
__ne__
__lt__
__gt__
__le__
__ge__
__add__
__sub__
__mul__
__floordiv__
__truediv__
__mod__
__pow__
__abs__
__len__
__getitem__
__contains__
__iter__
__next__
__call__
__hash__
"""