"""
Synthax:
Lambda arguments: expression
"""

# Example 1
add10 = lambda x: x + 10

print(add10(5))

# Example2 

mult = lambda x, y: x * y

print(mult(2, 7))

# Example 3

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]

# The points are sorted by the sum of the 2 points
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])

print("points2D:", points2D)
print("points2D sorted by y:", points2D_sorted)