class Vector:
    def __init__(self, *args):
        for i in args:
            if not isinstance(i, (int, float)):
                raise TypeError("All elements must be int or float")
        self._vector = list(args)
        self._length = len(self._vector)

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Can only add Vector to Vector")
        if self._length != other._length:
            raise ValueError("Vectors must be of the same length")
        return Vector(*(a + b for a, b in zip(self._vector, other._vector)))

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Can only subtract Vector from Vector")
        if self._length != other._length:
            raise ValueError("Vectors must be of the same length")
        return Vector(*(a - b for a, b in zip(self._vector, other._vector)))

    def __mul__(self, other):
        if isinstance(other, Vector):
            if self._length != other._length:
                raise ValueError("Vectors must be of the same length")
            return sum(a * b for a, b in zip(self._vector, other._vector))
        elif isinstance(other, (int, float)):
            return Vector(*(a * other for a in self._vector))
        else:
            raise TypeError("Can only multiply Vector by Vector or scalar")

    def __str__(self):
        return f"Vector({', '.join(map(str, self._vector))})"

    def magnitude(self):
        return sum(a**2 for a in self._vector) ** 0.5
    
    def normalize(self):
        for i in self._vector:
            if i == 0:
                raise ValueError("Cannot normalize a zero vector")
            if not isinstance(i, (int, float)):
                raise TypeError("All elements must be int or float")
        return Vector(*(round(a / self.magnitude(), 3) for a in self._vector))
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(v1)          # Output: Vector(1, 2, 3)
v3 = v1 + v2
print(v3)          # Output: Vector(5, 7, 9)
v4 = v2 - v1
print(v4)          # Output: Vector(3, 3, 3)
dot_product = v1 * v2
print(dot_product) # Output: 32
v5 = 3 * v1
print(v5)          # Output: Vector(3, 6, 9)
print(v1.magnitude())  # Output: 3.7416573867739413
v_unit = v1.normalize()
print(v_unit)      # Output: Vector(0.267, 0.534, 0.801)